#Road Segmentation
Road Segmentation is the classification of each road segment of the road network into highway road type and local road type. 
This is required so that we can define separate threshold values for each (depending on the road type) for proper congestion detection.

Each road segments/edges have the following attributes (contained in “road_table_name” table of the “road_network” database)
road_table_name:
 gid  | class_id | length        |      length_m      |                     name                     | source | target |     x1      |     y1     |     x2      |     y2     |         cost          |     reverse_cost      |       cost_s        |   reverse_cost_s    | rule | one_way | maxspeed_forward | maxspeed_backward |  osm_id   | source_osm | target_osm | priority |  
where,
gid: ID no. of the given road segment
class_id : ID no. of the different road types  

“osm_way_classes” table has the following attributes:
class_id | type_id |       name        | priority | default_maxspeed 
where,
name : the different types of road segment data available (viz. lane , opposite, opposite_lane, track, bridleway, bus_guideway, byway, cycleway, footway, living_street, motorway, motorway_junction, motorway_link, path, pedestrian, primary, primary_link, residential, road, secondary, secondary_link, service, services, steps, tertiary tertiary_link, track, trunk, trunk_link, unclassified, roundabout, grade1, grade2, grade3, grade4, grade5)

Information was sought manually from the following links to classify if a road type falls under ‘highway’ category or ‘local’ category:

http://wiki.openstreetmap.org/wiki/Map_Features
http://wiki.openstreetmap.org/wiki/Key:highway
http://wiki.openstreetmap.org/wiki/Highway_link
http://wiki.openstreetmap.org/wiki/Key:highway#Roads
http://wiki.openstreetmap.org/wiki/Key:highway#Paths

Using these, one-to-one correspondence was established through manual inspection between each ‘class_id’ (from ‘osm_way_classes’) and road category (highway/local). 
Based on the ‘class_id’ attribute and the corresponding road category (highway/local), each road segment/edge (using its ‘gid’ attribute from ‘road_table_name’) was classified as ‘highway’ or ‘local’.
With this all road segments of the road network has been segmented to highway and local.


