###FEATURE EXTRACTION

Road segmentation (i.e. classification of various road segments in the dataset to ‘highway’ or ‘local’) is followed by Feature Extraction. 

   Feature Extraction is necessary for proper labeling of the training examples as +ve or –ve , where +ve training examples are the ones corresponding to traffic congestion and –ve training examples are the ones corresponding to no traffic congestion. 
   The **no. of cars** and **average velocity of cars** are chosen as features for labeling the dataset. 
It has been reasoned that if the no. of cars in a bounding box are greater than a particular threshold value, there is congestion. Also, congestion occurs when the average velocity of cars is less than a particular threshold value. Chosen threshold values are different for highways and local roads. 
  Initially, the velocity at which a car travels via a particular edge and the number of cars travelled on that edge, are found out . For this purpose, the python script *car_edge_velocity_map.py* was executed. The input to the python script was the output of the segmentation part which is of the the form:<br/>

car_id |   date     |   time     |   longitude     |   latitude      | edge_id   |  road_type<br/>
39       2008-02-02    13:37:30     116.293690735     39.9227624928      73248       highway<br/>

The output generated is stored in a text file, *edge_id.txt* which contains the details of journey of a list of cars travelling on a particular edge along with their velocity information as:<br/>

car_id  |            time_interval                    |no. of cars  | edge_id     |  road_type   | total_distance  | average velocity<br/>
1324       2008-02-04 20:02:52   2008-02-04 20:07:53        1           39003        highway         301             9.2783361719 <br/>

The above output is input to the python script feature_extract.py, which gives the no. of cars within the specified interval  (say 5 mins) for a particular ‘edge_id’ and the average velocity of the cars as output in the form:<br/>

edge_id  | road_type   | no. of cars | average velocity<br/>
6367         highway         1         2.24944142652    <br/>

This output is stored in *feature_extracted.txt*<br/>
Once, the features is extracted then manually labeling of the datasets as +ve and –ve is done based on a particular threshold value (as described above). The python script *learning.py* takes *feature_extracted.txt* as input and generates output of the form:<br/>

edge_id | road_type | no. of cars | average velocity | label ( 0 = TRUE, 1 = FALSE)<br/>
6367          highway      1         2.24944142652       0<br/>

Here,  ‘0’ indicates no congestion and ‘1’ indicates a congestion.<br/>

##LEARNING

   Once, the dataset is classified as +ve and –ve, learning model is trained using the concept of K-nearest neighbours. Now, new examples are used to test the accuracy of the implemented model.<br/>  
In this way, the entire methodology was implemented for successful congestion detection.
