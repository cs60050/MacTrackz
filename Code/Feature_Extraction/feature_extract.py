'''__doc__ = 
usage: python2 feature_extract.py 
--Takes as input the output of car_edge_velocity_map 

The the input should be a list of  like this:

1401 2008-02-02 20:50:18 2008-02-02 20:55:18 1 highway 1795.39771416 300 5.9846590472
1324 2008-02-02 16:14:44 2008-02-02 16:15:30 1 highway 376.77262695 46 8.19070928152
1000 2008-02-05 20:35:57 2008-02-05 20:37:15 1 highway 351.137911473 78 4.50176809581
1027 2008-02-07 04:59:03 2008-02-07 05:04:03 1 highway 21.1433491227 300 0.0704778304091
1020 2008-02-04 02:29:18 2008-02-04 02:29:18 1 highway 0 0 0
1185 2008-02-02 16:14:07 2008-02-02 16:19:07 1 highway 898.761226876 300 2.99587075625
1231 2008-02-03 19:28:57 2008-02-03 19:33:57 1 highway 524.0477254 300 1.74682575133
    ...

---finding the number of cars within the specified interval (5 mins) for a paricular road_edge and computing the average velocity

the output featured_extracted.txt is a list that looks like

edgid road_type #cars avg_velocity

6367 highway 1 5.24944142652
6367 highway 1 1.16415563489
7220 local 1 2.95170824534
7220 local 1 2.25448309042
7051 highway 1 0.00334476032166
7238 local 1 3.02433231101
7238 local 1 0.0
7238 local 1 11.6266742781
7069 local 1 0.00761022573314
7069 local 1 12.1417941721
6398 highway 1 7.5170397724
6603 highway 1 1.82442533134
7332 local 1 0.0453340417108
7332 local 1 10.646939129
7332 local 1 7.30762075243
7332 local 1 5.60317740637'''

import sys
from collections import OrderedDict
import itertools
from operator import itemgetter
import filemapper as fm
import numpy
import math
from datetime import datetime
from geopy.distance import vincenty

def Sort_file(f):
        sequence = []
        sorted_ =[]
	with open("Edge1_/"+f,'r') as file_:
        	for line in file_:
        		line = line.replace('\n','')
           		data = line.split() 
                        print data
                       
        		sequence.append(data) 

                print sequence 
		sorted_ = sorted(sequence, key=itemgetter(1, 2))
        with open("Edge1_/"+f,'w') as out_file_: 
               for line in sorted_:
    			line_ = " ".join(str(elm) for elm in line)
    			out_data = line_+ ' \n' 
			print out_data
			out_file_.write(out_data)
        
	
	

def main(argv):
    print "\n"
    sequence = []
    
    
    
    all_files = fm.load('Edge1_') 
    for f in all_files:
         
         
         Sort_file(f)

    all_files = fm.load('Edge1_') 
    for f in all_files:
         sampling_time = 5 # in mins

         file_ = open("Edge1_/"+f,'r')
        



         line = file_.readline()
        
    	 data = line.split(' ')
         
         prev_time = data[1]+' '+data[2]
         date_format = "%Y-%m-%d %H:%M:%S"
         prev_time_  = datetime.strptime(prev_time, date_format)
         #print prev_time_
         no_cars =0
         avg_velocity = 0
         
         
 
	  
         for line in fm.read(f):
                
	        
		
    	 	line = line.replace('\n','')
    	 	data = line.split(' ')
                
		
		current_time= data[1]+' '+data[2]
                current_time_  = datetime.strptime(current_time, date_format)
                
		
                time_interval = current_time_ - prev_time_
                print time_interval
         	if time_interval.seconds < sampling_time*60:
                     no_cars = no_cars + 1
                     avg_velocity = avg_velocity+ float(data[9])
                     #print no_cars
                else:
		     dd = str(data[5]) +' '+str(data[6])+' ' + str(no_cars)+' '+str(avg_velocity/no_cars)+'\n'
		     print dd
		     prev_time_ = current_time_
                     
                     avg_velocity = float(data[9])
                     no_cars = 1
		     with open ('feature_extracted.txt','a') as outfile:
                     	outfile.write(dd)
	          
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
