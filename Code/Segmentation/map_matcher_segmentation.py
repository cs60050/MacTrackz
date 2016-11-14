'''__doc__ = 
usage: python2 map_matcher.py PSQL_URI ROAD_TABLE_NAME [SEARCH_RADIUS = 30] [MAX_ROUTE_DISTANCE = 2000] < sequence.txt

	python2 map_matcher.py "host=localhost port=5432 dbname=road_network user=OM password=OM" ROAD_TABLE_NAME [SEARCH_RADIUS = 30] [MAX_ROUTE_DISTANCE = 2000] < sequence_in_berlin.txt

The PSQL_URI looks like:
    "host=localhost port=5432 dbname=road_network user=postgres password=secret"

ROAD_TABLE_NAME is the table imported by osm2pgrouting.

SEARCH_RADIUS is a range value in meters within which the program will
search for each measurement's candidates. Think of it as GPS accuracy.

MAX_ROUTE_DISTANCE is the maximum allowed route distance (in meters)
between two concussive measurements.

The the input should be a list of coordinates like this:

    13.5258287 52.42294143
    13.52582773 52.42294161
    13.52582789 52.42294315
    13.5258275 52.42294331
    13.52571846 52.42293282
    13.52554795 52.42294917
    13.5255389 52.42301208
    13.52550688 52.4230304
    ...

Each line consists of a longtitude followed by a whitespace and then a
latitude.'''

'''modifications on 3/11/16 : addition of class_id and road_type'''

import sys
import psycopg2

import map_matching as mm
from map_matching.utils import Edge, Measurement
from itertools import izip


def generate_placeholder(length, width):
    """
    Generate "(%s, %s, %s, ...), ..." for placing parameters.
    """
    return ','.join('(' + ','.join(['%s'] * width) + ')' for _ in range(length))


def create_sequence_subquery(length, columns):
    """Create a subquery for sequence."""
    placeholder = generate_placeholder(length, len(columns))
    subquery = 'WITH sequence {columns} AS (VALUES {placeholder})'.format(
        columns='(' + ','.join(columns) + ')',
        placeholder=placeholder)
    return subquery


def query_edges_in_sequence_bbox(conn, road_table_name, sequence, search_radius):
    """
    Query all road edges within the bounding box of the sequence
    expanded by search_radius.
    """
    if not sequence:
        return

    subquery = create_sequence_subquery(len(sequence), ('lon', 'lat'))

    stmt = subquery + '''
    -- NOTE the length unit is in km
    SELECT edge.gid, edge.source, edge.target, edge.length * 1000, edge.length * 1000
    FROM {road_table_name} AS edge
         CROSS JOIN (SELECT ST_Extent(ST_MakePoint(sequence.lon, sequence.lat))::geometry AS extent FROM sequence) AS extent
    WHERE edge.the_geom && ST_Envelope(ST_Buffer(extent.extent::geography, %s)::geometry)
    '''.format(road_table_name=road_table_name)

    # Aggregate and flatten params
    params = sum([[lon, lat] for lon, lat in sequence], [])
    params.append(search_radius)

    cur = conn.cursor()
    cur.execute(stmt, params)

    for gid, source, target, cost, reverse_cost in cur.fetchall():
        edge = Edge(id=gid,
                    start_node=source,
                    end_node=target,
                    cost=cost,
                    reverse_cost=reverse_cost)
        yield edge
        
   
   
    cur.close()


def build_road_network(edges):
    """Construct the bidirectional road graph given a list of edges."""
    graph = {}

    # Graph with bidirectional edges
    for edge in edges:
        graph.setdefault(edge.start_node, []).append(edge)
        graph.setdefault(edge.end_node, []).append(edge.reversed_edge())

    return graph


# Subclass the native Candidate class to support more attributes
class Candidate(mm.Candidate):
    def __init__(self, measurement, edge, location, distance):
        super(Candidate, self).__init__(measurement=measurement, edge=edge, location=location, distance=distance) 
        '''modifications on 3/11/16 : addition of class_id and road_type'''
        self.lon = None
        self.lat = None
        self.class_id= None
        self.road_type= ''


def query_candidates(conn, road_table_name, sequence, search_radius):
    """
    Query candidates of each measurement in a sequence within
    search_radius.
    """
    subquery = create_sequence_subquery(len(sequence), ('id', 'lon', 'lat'))

    subquery = subquery + ',' + '''
    --- WITH sequence AS (subquery here),
    seq AS (SELECT *,
                   ST_SetSRID(ST_MakePoint(sequence.lon, sequence.lat), 4326) AS geom,
                   ST_SetSRID(ST_MakePoint(sequence.lon, sequence.lat), 4326)::geography AS geog
        FROM sequence)
    '''

    stmt = subquery + '''
    SELECT seq.id, seq.lon, seq.lat,
           --- Edge information
           edge.gid, edge.source, edge.target,
           edge.length, edge.length,

           --- Location, a float between 0 and 1 representing the location of the closest point on the edge to the measurement.
           ST_LineLocatePoint(edge.the_geom, seq.geom) AS location,

           --- Distance in meters from the measurement to its candidate's location
           ST_Distance(seq.geog, edge.the_geom::geography) AS distance,

           --- Candidate's location (a position along the edge)
           ST_X(ST_ClosestPoint(edge.the_geom, seq.geom)) AS clon,
           ST_Y(ST_ClosestPoint(edge.the_geom, seq.geom)) AS clat, 
           
           ---modifications on 3/11/16 : addition of class_id and road_type
            --- Class_id(class id of all the roads)
            edge.class_id
            
            --- Type_of_road(classification of roads)
           

    FROM seq CROSS JOIN {road_table_name} AS edge
    WHERE edge.the_geom && ST_Envelope(ST_Buffer(seq.geog, %s)::geometry)
          AND ST_DWithin(seq.geog, edge.the_geom::geography, %s)
    '''.format(road_table_name=road_table_name)

    # Aggregate and flatten params
    params = sum([[idx, lon, lat] for idx, (lon, lat) in enumerate(sequence)], [])
    params.append(search_radius)
    params.append(search_radius)

    cur = conn.cursor()
    cur.execute(stmt, params)
    '''modifications on 3/11/16 : addition of class_id and road_type'''
    for mid, mlon, mlat, eid, source, target, cost, reverse_cost, location, distance, clon, clat, class_id in cur:
 
        measurement = Measurement(id=mid, lon=mlon, lat=mlat)

        edge = Edge(id=eid, start_node=source, end_node=target, cost=cost, reverse_cost=reverse_cost)
        '''modifications begin'''
        if class_id in (101,102,103,104,105,106,107,108,109,124,125):
         road_type = 'highway'
        elif class_id in (110,111,112,113,114,115,116,117,118,119,120,121,122,301,303,304,305):
         road_type = 'local'
        else : road_type = 'others'
       
        assert 0 <= location <= 1
        candidate = Candidate(measurement=measurement, edge=edge, location=location, distance=distance)
        ''' modifications end'''
        # Coordinate along the edge (not needed by MM but might be
        # useful info to users)
        candidate.lon = clon
        candidate.lat = clat
        candidate.class_id = class_id
        candidate.road_type = road_type

        yield candidate

    cur.close()


def map_match(conn, road_table_name, sequence, search_radius, max_route_distance):
    """Match the sequence and return a list of candidates."""

    # Prepare the network graph and the candidates along the sequence
    edges = query_edges_in_sequence_bbox(conn, road_table_name, sequence, search_radius)
    network = build_road_network(edges)
    candidates = query_candidates(conn, road_table_name, sequence, search_radius)
    
    # If the route distance between two consive measurements are
    # longer than `max_route_distance` in meters, consider it as a
    # breakage
    matcher = mm.MapMatching(network.get, max_route_distance)

    # Match and return the selected candidates along the path
    return list(matcher.offline_match(candidates))


def parse_argv(argv):
    argv = argv[:] + [None, None]
    try:
        uri, road_table_name, search_radius, max_route_distance = argv[:4]
        search_radius = 30 if search_radius is None else int(search_radius)
        max_route_distance = 2000 if max_route_distance is None else int(max_route_distance)
    except ValueError:
        #print >> sys.stderr, __doc__
        return

    return uri, road_table_name, search_radius, max_route_distance


def main(argv):
    print "\n"
    params = parse_argv(argv)
    if not params:
        print "error"
        # Something is wrong
        return 1
    uri, road_table_name, search_radius, max_route_distance = params
    
    '''modifications start on 11/11/16 : reading raw file'''	
    sequence = []
    sequence_data = []
    print params[1]
    for line in sys.stdin:
    	line = line.replace('\r\n','')
    	data = line.split(',')
        outfile_ = str(data[0])+'_segmented.txt'
    	temp_data = [float(data[2]),float(data[3])]
        sequence.append(temp_data)
        sequence_data.append(data)
        
    	
    
    
    #sequence = [map(float, line.strip().split()) for line in sys.stdin if line.strip()]
    
    '''modifications end on 11/11/16 : reading raw file'''

    conn = psycopg2.connect(uri)
    candidates = map_match(conn, road_table_name, sequence, search_radius, max_route_distance)
    conn.close()
    
    '''modifications start on 11/11/16 : storing edge id and road type along with the raw data in a seperate file name - segmented_output.txt'''
    
    with open (outfile_,'w') as outfile:
        for line,candidate in izip(sequence_data,candidates):
    		line_ = " ".join(str(elm) for elm in line)
    		out_data = line_+ ' ' + str(candidate.edge.id) + ' ' + candidate.road_type +' '+ str(candidate.lon) +' '+ str(candidate.lat)+'\n'
		print out_data
		outfile.write(str(out_data))
    '''with open ('edge_cost.txt','a') as outfile:
        for candidate in candidates:
    		#line_ = " ".join(str(elm) for elm in line)
    		out_data = str(candidate.edge.id) + ' ' + str(candidate.edge.cost) + '\n'
		outfile.write(str(out_data))'''
   
    
    '''modifications end on 11/11/16 : storing edge id and road type along with the raw data in a seperate file name - segmented_output.txt'''

    for candidate in candidates:
        print '         Measurement ID: {0}'.format(candidate.measurement.id)
        print '             Coordinate: {0:.6f} {1:.6f}'.format(*map(float, (candidate.measurement.lon, candidate.measurement.lat)))
        print '    Matche d coordinate: {0:.6f} {1:.6f}'.format(*map(float, (candidate.lon, candidate.lat)))
        print '        Matched edge ID: {0}'.format(candidate.edge.id)
        print 'Location along the edge: {0:.2f}'.format(candidate.location)
        print '               Distance: {0:.2f} meters'.format(candidate.distance)
        '''modifications on 3/11/16 : addition of class_id and road_type'''
        print '               Class-ID: {0:.2f} '.format(candidate.class_id) 
        print '               Road_Type: {0:.10s} '.format(candidate.road_type)
        print

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
