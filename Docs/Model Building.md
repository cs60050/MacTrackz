###FEATURE EXTRACTION

Road segmentation (i.e. classification of various road segments in the dataset to ‘highway’ or ‘local’) is followed by Feature Extraction. 

   Feature Extraction is necessary for proper labeling of the training examples as +ve or –ve , where +ve training examples are the ones corresponding to traffic congestion and –ve training examples are the ones corresponding to no traffic congestion. 
   
   The **no. of cars** and **average velocity of cars** are chosen as features for labeling the dataset.
   
It has been reasoned that if the no. of cars in a bounding box are greater than a particular threshold value, there is congestion. Also, congestion occurs when the average velocity of cars is less than a particular threshold value. Chosen threshold values are different for highways and local roads. 

  Initially, the velocity at which a car travels via a particular edge and the number of cars travelled on that edge, are found out . For this purpose, the python script *car_edge_velocity_map.py* is executed. The input to the python script is the output of the segmentation part which is of the the form:<br/>

![](https://github.com/cs60050/MacTrackz/blob/master/Picture/1.PNG)

The output generated is stored in a text file, *edge_id.txt* which contains the details of journey of a list of cars travelling on a particular edge along with their velocity information as:<br/>

![](https://github.com/cs60050/MacTrackz/blob/master/Picture/2.png)

The above output is input to the python script feature_extract.py, which gives the no. of cars within the specified interval  (say 5 mins) for a particular ‘edge_id’ and the average velocity of the cars,  as output:<br/>

![](https://github.com/cs60050/MacTrackz/blob/master/Picture/3.png)

This output is stored in *feature_extracted.txt*<br/>

##LABELING

Once, the features are extracted, manually labeling of the datasets as +ve and –ve is done on the basis of particular threshold value (as described above). The python script *learning.py* takes *feature_extracted.txt* as input and generates output of the form:<br/>

![](https://github.com/cs60050/MacTrackz/blob/master/Picture/4.png)

Here,  ‘0’ indicates no congestion and ‘1’ indicates a congestion.<br/>

##LEARNING

   Once, the dataset is classified as +ve and –ve, learning model is trained using the concept of K-nearest neighbours. Now, new examples are used to test the accuracy of the implemented model.<br/> 
   
   K_NN has been run for 25 iterations. Classification results is output in a file named learning_results.csv
Below are the accuracy values for each iteration:

Accuracy: 92.96600234466588%<br/>
Accuracy: 92.76974416017798%<br/>
Accuracy: 93.57384441939121%<br/>
Accuracy: 93.38747099767981%<br/>
Accuracy: 93.89400921658986%<br/>
Accuracy: 91.79431072210066%<br/>
Accuracy: 93.279258400927%<br/>
Accuracy: 92.36812570145904%<br/>
Accuracy: 93.5022026431718%<br/>
Accuracy: 92.9316338354577%<br/>
Accuracy: 93.3993399339934%<br/>
Accuracy: 91.79954441913439%<br/>
Accuracy: 93.0%<br/>
Accuracy: 93.55932203389831%<br/>
Accuracy: 91.83222958057395%<br/>
Accuracy: 92.85714285714286%<br/>
Accuracy: 92.05448354143019%<br/>
Accuracy: 92.50851305334847%<br/>
Accuracy: 93.44632768361582%<br/>
Accuracy: 92.57990867579909%<br/>
Accuracy: 94.04630650496141%<br/>
Accuracy: 94.18221734357849%<br/>
Accuracy: 92.92134831460675%<br/>
Accuracy: 94.02628434886499%<br/>
Accuracy: 92.94947121034077%

In this way, the entire methodology was implemented for successful congestion detection.
