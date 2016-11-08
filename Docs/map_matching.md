
Map-matching is the process of aligning a sequence of observed user positions with the road network on a digital map. It is a 
fundamental pre-processing step of our work . We have implemented ST-Matching(bold/underline) algorithm which handles low-sampling-rate GPS trajectories .Advantage of using this algorithm is it cosiders

#### spatial geometric and topological structures of the road network.
#### the temporal/speed constraints of the trajectories.

Finally Based on spatio-temporal analysis, a candidate graph is constructed from which the best matching path sequence is identified.The major challenge is, as the distance between two neighboring points increases, less information can be used to deduce the precise locations of the objects. The problem is aggravated when a moving object is travelling with high speed, or there are many intersections between two observed neighboring points.To address this challenge ST-Matching algorithim provides two key observations as follows.

Observation 1: True paths tend to be direct, rather than roundabout.For example, consider the GPS trajectory of a taxi visualized in the following figure :
![](https://github.com/cs60050/MacTrackz/blob/master/Picture/Screenshot_1.jpg)
