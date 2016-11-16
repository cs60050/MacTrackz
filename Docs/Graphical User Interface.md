# Graphical User Interface


A Graphical User Interface has been designed using Leaflet JavaScript for OpenStreetMap. 
 Following technologies are used: <br/>
1.	PHP <br/>
2.	JavaScript <br/>
3.	AJAX <br/>
4.	Apache Server

The GUI initially designed is shown below:

![Image of GUI](https://github.com/cs60050/MacTrackz/blob/master/Picture/GUI.png)

 
It has three features:

**1.	Generating Bounding Box/Segmentation Region:**
	The GPS footprints (in *.json* format) are selected from the dropdown menu. 
	GPS footprints were plotted using the ‘Plot Input’ button .  
	A bounding box for congestion detection was created by clicking on ‘Output’ button 		which takes the output ofe road segmentation algorithm in *.json* format. The four   	 points of the Bounding-Box are in the order (NW,SW,SE,NE) in 4 consecutive lines of 	 *.json* file. The rectangular Bounding-Box was created from these points in the 	 	 background. 
Note - User may select multiple files in Input Button; in that case background color of those bounding boxes will be different! 

![](https://github.com/cs60050/MacTrackz/blob/master/Picture/Feature1_Input.png)

> (Plot of GPS Traces)


![](https://github.com/cs60050/MacTrackz/blob/master/Picture/Feature1_Output.png)

> (Bounding-Box, for congestion detection in a study region)


**2.	Visualisation of congestion detection:**
	Input is a range from 1 to 5.
	Using this feature, the congested ways in a study region are shown in a range of 1 to 	  5, where 1 represents the most congested way and 5 represents the least congested way 	in the segmented part. 
	Choosing any particular range value and clicking on ‘’Submit’ results in plotting of 	 all the .json files upto that range value, all in different colors i.e. all the road 	  segments starting from the most congested way upto that range are plotted. 
	This is shown below:
    
![](https://github.com/cs60050/MacTrackz/blob/master/Picture/Feature2_1.png)

 > (Range 1: Most congested way)



![](https://github.com/cs60050/MacTrackz/blob/master/Picture/Feature2_2.png)

   > (Range 2)



![](https://github.com/cs60050/MacTrackz/blob/master/Picture/Feature2_3.png)

   > (Range 3)
   
   

![](https://github.com/cs60050/MacTrackz/blob/master/Picture/Feature2_4.png)

   > (Range 4)
   
   

![](https://github.com/cs60050/MacTrackz/blob/master/Picture/Feature2_5.png)

   > (Range 5: All possible congestion levels)

**3.	Finding Alternate Route:**
	In case of a traffic congestion, alternate route is suggested using this feature.  


![](https://github.com/cs60050/MacTrackz/blob/master/Picture/Feature3_input.png)

> (Plot Input)


![](https://github.com/cs60050/MacTrackz/blob/master/Picture/Feature3_output.png)

> (Plot Output)

