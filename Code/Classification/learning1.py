import os
import shutil
import datetime

def learning (path,filename):
	avg_val_threshold_local = 1.0
	no_vehicle_threshold_local = 1
	avg_val_threshold_highway = 1.5
	no_vehicle_threshold_highway = 1
	with open (path + '//learning.txt','w') as outfile:
		with open (path + '//' + filename,'r') as infile:
			for line in infile:
				words = line.split(' ')
				if words[1] == 'highway':
					if int(words[2]) > no_vehicle_threshold_highway and float(words[3].replace('\n','')) <  avg_val_threshold_highway:
						congestion = 1 #true	
					else:
						congestion = 0 #false
				else:
					if int(words[2]) > no_vehicle_threshold_local and float(words[3].replace('\n','')) <  avg_val_threshold_local:
						congestion = 1 #true	
					else:
						congestion = 0 #false
				data = words[0] + ',' + words[1] + ',' + words[2] + ',' + words[3].replace('\n','') + ',' + str(congestion) + '\n'
				outfile.write(data)
			

def main():
	path = raw_input('Enter Path:')
	filename = raw_input('Enter Feature Extreacted filename (with extraction):')
	learning(path,filename)
	
if __name__=='__main__':
	main()	
