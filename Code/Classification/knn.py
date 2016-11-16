import csv
import random
import math
import operator
import time

def loadDataset(filename, split, trainingSet=[] , testSet=[]):
    with open(filename, 'rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)):
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])


def euclideanDistance(instance1, instance2, length):
	distance = 0
	#print instance1
	#print instance2
	for x in range(length):
		if x == 2 or x == 3:
			distance += pow((float(instance1[x]) - float(instance2[x])), 2)
	return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        #print dist
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0
    
def main():
    #prepare data
	#path = raw_input('Enter Path:') 
	iteration = raw_input('Enter iterations:')
	for i in range(int(iteration)):
		trainingSet=[]
		testSet=[]
		split = 0.67
		#loadDataset(path + '//learning.txt', split, trainingSet, testSet)
                loadDataset('learning.txt', split, trainingSet, testSet)
		#with open(path + '//learning_results.csv','a') as f:
                with open('learning_results.csv','a') as f:
			f.write(time.strftime("%c") + ' \n')
			f.write('Train set: ' + repr(len(trainingSet)) + '\n')
			f.write('Test set: ' + repr(len(testSet)) + '\n')
			# generate predictions
			predictions=[]
			k = 3
			for x in range(len(testSet)):
				neighbors = getNeighbors(trainingSet, testSet[x], k)
				result = getResponse(neighbors)
				predictions.append(result)
				f.write(str(testSet[x]) + '\n')
				f.write('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]) + '\n')				
			accuracy = getAccuracy(testSet, predictions)
			f.write('Accuracy: ' + repr(accuracy) + '%\n\n')
			print('Accuracy: ' + repr(accuracy) + '%')  
			
if __name__=='__main__':
	main()			
