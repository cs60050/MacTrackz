### Data Description

This  dataset  contains  the  GPS  trajectories  of  10,357  taxis  during  the  period  of  Feb.   2  to  Feb.   8,  2008
within  Beijing.   The  total  number  of  points  in  this  dataset  is  about  15  million  and  the  total  distance  of
the trajectories reaches to 9 million kilometers.  Fig. 1 plots the distribution of time interval and distance
interval between two consecutive points.  The average sampling interval is about 177 seconds with a distance
of about 623 meters.  Each  le of this dataset, which is named by the taxi ID, contains the trajectories of
one taxi.  Fig. 2 visualizes the density distribution of the GPS points in this dataset.

![](https://github.com/cs60050/MacTrackz/blob/master/Picture/Dataset_1.jpg)

![](https://github.com/cs60050/MacTrackz/blob/master/Picture/dataset_2.jpg)

### Here is a piece of sample in a  file

1,2008-02-02 15:36:08,116.51172,39.92123</br>
1,2008-02-02 15:46:08,116.51135,39.93883</br> 
1,2008-02-02 15:46:08,116.51135,39.93883</br>
1,2008-02-02 15:56:08,116.51627,39.91034</br>
1,2008-02-02 16:06:08,116.47186,39.91248</br>
1,2008-02-02 16:16:08,116.47217,39.92498</br>
1,2008-02-02 16:26:08,116.47179,39.90718</br>
1,2008-02-02 16:36:08,116.45617,39.90531</br>
1,2008-02-02 17:00:24,116.47191,39.90577</br>
1,2008-02-02 17:10:24,116.50661,39.9145</br>
1,2008-02-02 20:30:34,116.49625,39.9146</br>

Each line of a file has the following elds, separated by comma: taxi id, date time, longitude, latitude .
