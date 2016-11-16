
### Solution Overview : 

We have divided our work in four stages.

#### Map Matching :<br/>
Map-matching is the process of aligning a sequence of observed user positions with the road network on a digital map. It is a fundamental pre-processing step of our work . We have implemented ST-Matching(bold/underline) algorithm which handles low-sampling-rate GPS trajectories .

#### Segmentation :<br/>
As we are using the unlebelled data, we need to label it first. Road Segmentation is the classification of each road segment of the road network into highway road type and local road type. to define threshold values for congestion detection of each road type seperately.

#### Learning : <br/>
In this part we have extracted various features and experimented with different threshold values. We are using two road types namely 'highway' and 'local' . we have used two different threshold values for these two kind of road .Finally we have classified the data as congested or not.

#### GUI : <br/>
Our GUI module is responsible for displaying the whole thing i.e. plotting the GPS traces on road , visualising the congested region etc . 

