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
Once, the features are extracted, labeling of the datasets as +ve and –ve is done manually on the basis of particular threshold value (as described above). The python script learning.py takes feature_extracted.txt as input and generates output of the form:

![](https://github.com/cs60050/MacTrackz/blob/master/Picture/4.png)

Here, ‘0’ indicates no congestion and ‘1’ indicates a congestion.

##MODEL BUILDING:
Once, the dataset is classified as +ve and –ve, a portion is classified as ‘Training Data Set’ and the remaining as ‘Test Data Set’. 
In our work,  1195 examples constituted the ‘Training Data Set’. The learning model is trained using the concept of K-nearest neighbours with training examples from the ‘Training Data Set’. 

##MODEL VALIDATION:
The model is validated using the ‘Test Data Set’. The ‘Test Data Set’ is comprised of 853 examples. Specifically, model is run for 25 iterations and accuracy of the model (in terms of % of examples correctly classified) is calculated. The results are tabulated in the [“Results”](https://github.com/cs60050/MacTrackz/blob/master/Docs/Learning%20Accuracy%20and%20Results.md) section.

In this way, the entire methodology is implemented for successful congestion detection.

