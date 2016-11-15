'''__doc__ = 
usage: python2 car_edge_velocity_map.py  

---finding out at what velocity a car travels at this particular edge and how many such car exists

---it take as input the segmented files. 	

The input should be a list of coordinates like this:

car_id start_date_time end_dte_ttime longitude latitude edge_id road_type   
39 2008-02-02 13:37:30 73248 highway 116.293690735 39.9227624928
39 2008-02-02 13:40:17 65747 highway 116.280149159 39.9231665487
39 2008-02-02 13:45:17 65747 highway 116.280647231 39.9231569104
39 2008-02-02 13:45:17 65747 highway 116.280647231 39.9231569104
39 2008-02-02 13:49:15 65747 highway 116.28011801 39.9231671515
39 2008-02-02 13:54:15 4469 highway 116.303339663 39.9225681601
39 2008-02-02 13:59:15 50274 highway 116.318009364 39.9373923476
39 2008-02-02 14:08:09 64832 highway 116.34543552 39.9385293268
    ...'''

''' The output is edge_id.txt that conatins the details of journey of a list of car travelling at this particular edge along with their velocity information like this:

car_id time_interval edge_id road_type total_distance velocity

1324 2008-02-04 20:02:52 2008-02-04 20:07:53 39003 highway 2792.77918774 301 9.2783361719
1211 2008-02-03 00:58:23 2008-02-03 01:03:23 39003 highway 4561.75099144 300 15.2058366381
1211 2008-02-04 10:56:19 2008-02-04 11:01:19 39003 highway 1673.12430594 300 5.57708101981
1106 2008-02-06 18:04:29 2008-02-06 18:11:26 39003 highway 1846.93697259 417 4.42910544985
39 2008-02-06 05:16:55 2008-02-06 05:21:55 39003 highway 8.26177269811 300 0.027539242327
--'''



import sys
from collections import OrderedDict
import itertools
from operator import itemgetter
import filemapper as fm
import numpy
import math
from datetime import datetime
from geopy.distance import vincenty

def main(argv):
    print "\n"
    sequence = []
    
    
    
    all_files = fm.load('Segmented') 
    for f in all_files:
         
         
         file_ = open("Segmented/"+f,'r')
         
         line = file_.readline()
         #line = line.replace('\n','')
    	 data = line.split(' ')
         print str(data[0])
         prev_location = (float(data[3]),float(data[4]))
         prev_time = data[1]+' '+data[2]
         date_format = "%Y-%m-%d %H:%M:%S"
         prev_time1  = datetime.strptime(prev_time, date_format)
         prev_edge_id = data[5]
         prev_road_type = data[6]
         prev_distance = 0
         prev_duration = 0
         velocity = 0
         
         
 
	  
         for line in fm.read(f):
                
	        
		
    	 	line = line.replace('\n','')
    	 	data = line.split(' ')
		current_location = (float(data[3]),float(data[4]))
		current_time= data[1]+' '+data[2]
                current_time_  = datetime.strptime(current_time, date_format)
                current_edge_id = data[5]
		
                distance = (vincenty(current_location,prev_location).meters)
		prev_distance = prev_distance+distance
         	if prev_edge_id != current_edge_id:
                     
		
                     time_duration = current_time_-prev_time1
                     d = str(data[0]) +' '+str(prev_time1)+' ' + str(current_time_)+' '+str(prev_edge_id)+' '+str(prev_road_type)+' '+str(prev_distance) + ' ' + str(time_duration.seconds)
		     print d
                     if time_duration.seconds == 0: prev_distance =0
                     
                     if (prev_distance == 0) or (time_duration.seconds ==0): velocity = 0
                     else: velocity = prev_distance/ time_duration.seconds
                    
               	     dd = str(data[0]) +' '+str(prev_time1)+' ' + str(current_time_)+' '+str(prev_edge_id)+' '+str(prev_road_type)+' '+str(prev_distance) + ' ' + str(time_duration.seconds) +' ' + str(velocity)+'\n'
                     prev_road_type = data[6]
                     prev_distance = 0
                     prev_duration = 0
                     prev_time1 = current_time_
                     edge_file = 'Edge/'+str(prev_edge_id)+'.txt'
                     
		     with open (edge_file,'a') as outfile:
           	     	outfile.write(dd)
		prev_edge_id = current_edge_id
                prev_location = current_location
               
                
		                  
                    
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
