### Problem

#### Data

Load the data set nycflights_full.csv. This is data on about 336000 flights during the year 2013. The data is in three pieces - nycflights_full_p1.csv, nycflights_full_p2.csv, nycflights_full_p3.csv. You need to put these together by concatenating them - they all contain the same columns, and there is no duplication of records among these data sets.

**Note that there are NAs in this data set: deal with them appropriately.**


#### Tasks
<ol>
<li>Find out the number of flights for each day of the week</li>
<li>Find the average distance, total distance and number for all delayed flights on Friday (Note that we need to define what is meant by “delayed”, and create an indicator variable for this)</li>
<li>Find out how many flights were on time on weekdays and weekends (Consider Saturday and Sunday as weekends)</li>
<li>Find out the number of flights for each destination across all weekdays (i.e. Monday to Friday)</li>
<li>Find number of delayed flights by distance and origin (you need to convert the continuous numeric variable distance into a categoric variable)</li>
</ol>

import numpy as np
import pandas as pd
d1 = pd.read_csv('../pydata/nycflights_full_p1.csv')
d2 = pd.read_csv('./pydata/nycflights_full_p2.csv') 
d3 = pd.read_csv('./pydata/nycflights_full_p3.csv')
nyc_full = pd.concat([d1,d2,d3], axis=0)
nycf =  nyc_full.dropna()

