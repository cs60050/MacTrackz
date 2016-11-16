import os
import shutil
import datetime
import sys

def learning (filename):
        sequence =[]
	avg_val_threshold_local = 8
	no_vehicle_threshold_local = 1
	avg_val_threshold_highway = 20
	no_vehicle_threshold_highway = 2
        '''with open (filename,'r') as infile:
			for line in infile:
				words = line.split(' ')
                                sequence.append(words[0],words[2])'''
	with open ('learning1.txt','w') as outfile:
		with open (filename,'r') as infile:
			for line in infile:
				words = line.split(' ')
                                
				if words[1] == 'highway':
					if int(words[2]) > no_vehicle_threshold_highway and float(words[3]) <  avg_val_threshold_highway:
						congestion = 1 #true	
					else:
						congestion = 0 #false
				else:
					if int(words[2]) > no_vehicle_threshold_local and float(words[3]) <  avg_val_threshold_local:
						congestion = 1 #true	
					else:
						congestion = 0#false
				data = str(words[0]) + ',' + str(words[1]) + ',' + str(words[2]) + ',' + str(words[3].replace('\n','')) + ',' + str(congestion) + '\n'
			        print data				
				outfile.write(data)
			

def main(argv):
	#path = raw_input('Enter Path:')
	filename ='feature_extracted_.txt' #raw_input('Enter Feature Extreacted filename (with extraction):')
        print filename

	learning(filename)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
