###ROAD SEGMENTATION
Road Segmentation is the classification of each road segment of the road network into **highway road type** and **local road type**. 
to define threshold values for congestion detection of each road type seperately.

Each road segment/edge has the following attributes (table name: “road_table_name”; database name: “road_network”)
road_table_name:

 gid</br>class_id</br>length</br>length_m name</br>source</br>target</br>x1</br>y1</br>x2</br>y2</br>cost</br>reverse_cost</br>cost_s</br>reverse_cost_s</br>rule</br>one_way</br>maxspeed_forward</br>osm_id</br>source_osm</br>target_osm</br>priority|
 :-------------------------------------------------------------

where,</br>
gid: ID no. of the given road segment </br>
class_id : ID no. of different road types  

“osm_way_classes” table has the following attributes:

class_id</br>type_id</br>name</br>priority</br>default_maxspeed |
:------------------------------------------------------------
where,</br>
name : different types of road segment </br> 
(viz. lane , opposite, opposite_lane, track, bridleway, bus_guideway, byway, cycleway, footway, living_street, motorway, motorway_junction, motorway_link, path, pedestrian, primary, primary_link, residential, road, secondary, secondary_link, service, services, steps, tertiary tertiary_link, track, trunk, trunk_link, unclassified, roundabout, grade1, grade2, grade3, grade4, grade5)

Information has been collected from the following links to classify road type into ‘highway’ and ‘local’:

http://wiki.openstreetmap.org/wiki/Map_Features
http://wiki.openstreetmap.org/wiki/Key:highway
http://wiki.openstreetmap.org/wiki/Highway_link
http://wiki.openstreetmap.org/wiki/Key:highway#Roads
http://wiki.openstreetmap.org/wiki/Key:highway#Paths

By manual inspection, one-to-one correspondence has been established between each ‘class_id’ (table: ‘osm_way_classes’) of road segments and road category (highway/local). 
Based on the ‘class_id’ attribute of each road segment and the corresponding road category (highway/local), each road segment/edge (using its ‘gid’ attribute from ‘road_table_name’) has been classified as **highway** or **local**.



