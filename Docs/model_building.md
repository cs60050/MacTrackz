After the road segmentation i.e. classifying the various road segments in the dataset as corresponding to ‘highway’ or ‘local’, Feature Extraction was carried out. Feature Extraction was necessary for proper labeling of the training examples as +ve or –ve , where +ve training examples are the ones corresponding to traffic congestion and –ve training examples are the ones corresponding to no traffic congestion. The **no. of cars** and **average velocity of cars** were chosen as features for labeling the dataset. We have reasoned that if the no. of cars in a bounding box are greater than a particular threshold value, there is a congestion. Also, congestion occurs when the average velocity of cars is less than a particular threshold. The threshold values chosen were different for highways and local roads. 
Initially, the velocity at which a car travels at a particular edge and how many such cars exist was found out. For this purpose, the python script *car_edge_velocity_map.py* was executed. The input to the python script was the output of the segmentation part which was of the the form:<br/>
car_id |   date   |   time   |   longitude     |   latitude    | edge_id   |  road_type<br/>
39     | 2008-02-02 |  13:37:30  |  116.293690735  |  39.9227624928  |   73248   |    highway<br/>
The output generated was stored in a text file, *edge_id.txt* which contains the details of journey of a list of cars travelling at a particular edge along with their velocity information as:<br/>

car_id |   time_interval   |no. of cars| edge_id   |    road_type   | total_distance | average velocity<br/>
1324      |  2008-02-04 20:02:52   | 2008-02-04 20:07:53  |   1   |   39003  |    highway |     301 9.2783361719 <br/>

The above output was input to the python script feature_extract.py which gave the output the no. of cars within the specified interval  (say 5 mins) for a particular ‘edge_id’ and the average velocity of the cars in the form:<br/>
edge_id | road_type | no. of cars | average velocity<br/>
6367          highway               1           2.24944142652    <br/>
This output was stored in *feature_extracted.txt*
Once, the features were extracted then we manually label the datasets as +ve and –ve based on a particular threshold value (as described before). The python script *learning.py* takes *feature_extracted.txt* as input and generates output of the form:
edge_id | road_type | no. of cars | average velocity | label ( 0 = TRUE, 1 = FALSE)
6367          highway               1           2.24944142652           0
Here,  ‘0’ indicates no congestion and ‘1’ indicates a congestion.
Once, the dataset was classified as +ve and –ve, we train our learning model using the concept of K-nearest neighbours. Now, new examples are used to test the accuracy of the implemented model.  
In this way, the entire methodology was implemented for successful congestion detection.
