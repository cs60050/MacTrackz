### MAP MATCHING

Map-matching is the process of aligning a sequence of observed user positions with the road network on a digital map. It is a 
fundamental pre-processing step of our work . We have implemented ST-Matching(bold/underline) algorithm which handles low-sampling-rate GPS trajectories .Advantage of using this algorithm is, it cosiders :

A. spatial geometric and topological structures of the road network.<br/>B. the temporal/speed constraints of the trajectories.<br/>

Finally Based on spatio-temporal analysis, a candidate graph is constructed from which the best matching path sequence is identified.The major challenge is, as the distance between two neighboring points increases, less information can be used to deduce the precise locations of the objects. The problem is aggravated when a moving object is travelling with high speed, or there are many intersections between two observed neighboring points.To address this challenge ST-Matching algorithim provides two key observations as follows.

Observation 1: True paths tend to be direct, rather than roundabout.For example, consider the GPS trajectory of a taxi 
visualized in the following figure :

![](https://github.com/cs60050/MacTrackz/blob/master/Picture/Observation_1.jpg)


Observation 2: True paths tend to follow the speed constraints of the road. For Example, consider another taxi GPS trajectory visualized in the Figure below. Without speed information, it is nearly impossible to tell whether these two points belong to the highway or the service road. This algorithm computes the average speed of this path as 80km/h based on distance of the two points and their timestamps, and determines that the two points are very likely on the highway. Clearly this approach cosiders temporal/speed information in the matching process.

![](https://github.com/cs60050/MacTrackz/blob/master/Picture/Observation_2.jpg)

The architecture of our proposed map-matching system is shown in the following figure . It is composed of three major components: Candidate Preparation, Spatial and Temporal Analysis, and Result Matching.
 ![](https://github.com/cs60050/MacTrackz/blob/master/Picture/System_structure.jpg)
 
###  Candidate Preparation :
This component contains a road network database with indexed edge and vertex information. It accepts given raw GPS trajectory from the user, and then retrieves all the possible candidate points for each sampling point on the trajectory. This step can be efficiently performed with the built-in grid-based spatial index. The output of this component is a set of candidate points and the candidate road segments they lie on.

![](https://github.com/cs60050/MacTrackz/blob/master/Picture/candidate_prep.jpg)

### Spatial and Temporal Analysis :
This component performs spatial analysis followed by temporal analysis on the retrieved candidate sets and the trajectory to be matched. Spatial analysis not only considers the distance between a single GPS point and the candidate road segments for this
point, but also takes into account the topological information of the road network. To avoid roundabout paths, we employ
shortest path to measure the similarity between each candidate path and the “true” path.

Temporal analysis measures the actual average travel speed between any neighboring points. It then compares the
average speed with the typical speed constraints on each candidate path. The information can later be used to match
the trajectory to the candidate path with most similar speed conditions during that time interval.

After spatial and temporal analysis, a candidate graph is constructed as the output of this component. The nodes of the graph are the set of candidate points for each GPS observation, and the edges of the graph are set of shortest paths between any
two neighboring candidate points. The nodes and edges are all assigned weight values based on the results of spatial/temporal
analysis.

### Result Matching :
This component evaluates the candidate graph using the weight information assigned during spatial/temporal analysis. It matches given trajectory to the path with highest score in the candidate graph. The results are then visualized on an interface that can be tailored towards different end-user devices. The results can also be stored in a traffic database to support external applications such as traffic management or driving directions.

#### ALGORITHMS
![](https://github.com/cs60050/MacTrackz/blob/master/Picture/ST-Matching_algo.jpg)
![](https://github.com/cs60050/MacTrackz/blob/master/Picture/Find_matched_seq_algo.jpg)


### SEGMENTATION
As we are using unlabeled data we need to label the data using segmentation technique. Following is the sample input and output of the segmentation modulue . 

##### Input :<br/> 
39 2008-02-06 07:31:55 116.471568972 40.0006777559 61215 <br/>
39 2008-02-06 07:36:55 116.466551456 39.9824077548 21555 <br/>
39 2008-02-06 07:41:55 116.470695969 39.9797347746 50440 <br/>
39 2008-02-06 07:46:55 116.488400567 39.9640832163 46033 <br/>
39 2008-02-06 07:51:55 116.488391242 39.9650774185 86599 <br/>
39 2008-02-06 07:56:55 116.497140056 39.9640600262 3858 <br/>
39 2008-02-06 08:01:55 116.497266254 39.9629016765 3858 <br/>
39 2008-02-06 08:06:55 116.483357363 39.9521418857 78516 <br/>
39 2008-02-06 08:11:55 116.473850089 39.906719755 26757 <br/>
39 2008-02-06 08:16:55 116.474930049 39.9067165233 32537 <br/>
39 2008-02-06 08:21:55 116.484704567 39.9109855982 22878 <br/>
39 2008-02-06 08:31:57 116.485587202 39.9116563146 46451 <br/>
39 2008-02-06 08:36:55 116.456749944 39.9073077324 9739 <br/>

##### Output <br/>
39 2008-02-06 07:31:55 116.471568972 40.0006777559 61215 highway<br/>
39 2008-02-06 07:36:55 116.466551456 39.9824077548 21555 highway<br/>
39 2008-02-06 07:41:55 116.470695969 39.9797347746 50440 highway<br/>
39 2008-02-06 07:46:55 116.488400567 39.9640832163 46033 others<br/>
39 2008-02-06 07:51:55 116.488391242 39.9650774185 86599 others<br/>
39 2008-02-06 07:56:55 116.497140056 39.9640600262 3858 highway<br/>
39 2008-02-06 08:01:55 116.497266254 39.9629016765 3858 highway<br/>
39 2008-02-06 08:06:55 116.483357363 39.9521418857 78516 highway<br/>
39 2008-02-06 08:11:55 116.473850089 39.906719755 26757 highway<br/>
39 2008-02-06 08:16:55 116.474930049 39.9067165233 32537 highway<br/>
39 2008-02-06 08:21:55 116.484704567 39.9109855982 22878 local<br/>
39 2008-02-06 08:31:57 116.485587202 39.9116563146 46451 local<br/>
39 2008-02-06 08:36:55 116.456749944 39.9073077324 9739 highway<br/>

