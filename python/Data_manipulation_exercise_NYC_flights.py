#!/usr/bin/env python
# coding: utf-8

# # Python data manipulation exercise - NYC flights data

# ### Problem
# 
# #### Data
# 
# Load the data set nycflights_full.csv. This is data on about 336000 flights during the year 2013. The data is in three pieces - nycflights_full_p1.csv, nycflights_full_p2.csv, nycflights_full_p3.csv. You need to put these together by concatenating them - they all contain the same columns, and there is no duplication of records among these data sets.
# 
# **Note that there are NAs in this data set: deal with them appropriately.**
# 
# 
# #### Tasks
# <ol>
# <li>Find out the number of flights for each day of the week</li>
# <li>Find the average distance, total distance and number for all delayed flights on Friday (Note that we need to define what is meant by “delayed”, and create an indicator variable for this)</li>
# <li>Find out how many flights were on time on weekdays and weekends (Consider Saturday and Sunday as weekends)</li>
# <li>Find out the number of flights for each destination across all weekdays (i.e. Monday to Friday)</li>
# <li>Find number of delayed flights by distance and origin (you need to convert the continuous numeric variable distance into a categoric variable)</li>
# </ol>

# In[1]:


import numpy as np
import pandas as pd


# 

# In[88]:


d1 = pd.read_csv('./Data/nycflights_full_p1.csv')
d2 = pd.read_csv('./Data/nycflights_full_p2.csv') 
d3 = pd.read_csv('./Data/nycflights_full_p3.csv')


# In[89]:


d1.shape


# In[90]:


d2.shape


# In[91]:


d3.shape


# In[92]:


d3.columns


# In[93]:


#to concat
nyc_full = pd.concat([d1,d2,d3], axis=0)


# In[94]:


nyc_full.head()


# In[95]:


nyc_full.shape


# In[96]:


nyc_full.columns


# In[97]:


nyc_full.describe()


# In[98]:


nyc_full.info()


# In[99]:


nyc_full.isnull().sum()


# In[100]:


nycf =  nyc_full.dropna()


# In[101]:


nycf.shape


# In[102]:


(336472 - 327052)*100 /336472


# In[103]:


## this much is okay. 


# In[107]:


nycf['date'] = pd.to_datetime(nycf['date'])


# In[110]:


nycf.head()


# In[111]:


nycf['day'] = nycf['date'].dt.dayofweek


# In[112]:


nycf.head()


# In[113]:


days_code = {0:'Monday',1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
days_code


# In[114]:


nycf['day'] = nycf['day'].map(days_code)


# In[115]:


nycf.head()


# In[116]:


nycf_gr = nycf.groupby('day')


# In[117]:


nycf_gr


# In[118]:


nycf_gr.day.count()


# In[124]:


nycf['status'] = np.where((nycf['dep_delay'] > 15) | (nycf['arr_delay'] > 15),'delayed','ontime')


# In[125]:


nycf.head()


# In[126]:


nycf_fri = nycf[(nycf['day']=='Friday') & (nycf['status'] == 'delayed')]


# In[127]:


nycf_fri.shape


# In[133]:


print('avg number of miles %.1f miles' % nycf_fri.distance.mean())
print('The total distance of %d miles' % nycf_fri.distance.sum())
print('The number of delayed flights on Friday %d' % nycf_fri.shape[0])


# In[135]:


nycf['day_type'] = np.where((nycf['day'] == 'Saturday') | (nycf['day'] == 'Sunday'), 'weekend', 'weekday')


# In[137]:


nycf.head(10)


# In[145]:


nycf_subset_ontime = nycf[nycf['status'] == 'ontime']


# In[149]:


nycf_subset_ontime_gr = nycf_subset_ontime.groupby('day_type')


# In[150]:


nycf_subset_ontime_gr.day_type.count()


# In[151]:


nycf_subset_Weekday = nycf[nycf['day_type'] == 'weekday']


# In[152]:


nycf_subset_Weekday.head()


# In[154]:


nycf_week_dest_gr = nycf_subset_Weekday.groupby('dest')


# In[155]:


nycf_week_dest_gr.dest.count()


# In[167]:


import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(15,7))
nycf_week_dest_gr.dest.count().plot(ax=ax)


# In[168]:


#Find number of delayed flights by distance and origin 
#(you need to convert the continuous numeric variable distance into a categoric variable)


# In[169]:


nycf_subset_delayed = nycf[nycf['status'] == 'delayed']


# In[170]:


nycf_subset_delayed.head()


# In[171]:


dist_p33 = np.percentile(nycf.distance,33)


# In[172]:


nycf['distcat'] = 'Medium'


# In[173]:


nycf.distcat[nycf.distance < dist_p33] = 'Short'


# In[174]:


dist_p67 = np.percentile(nycf.distance, 67)


# In[175]:


nycf.distcat[nycf.distance < dist_p67] = 'Long'


# In[179]:


nycf.head()


# In[181]:


nycf_subset_delayed = nycf[nycf['status'] == 'delayed']


# In[182]:


nycf_subset_delayed.head()


# In[183]:


nyc_Gr = nycf_subset_delayed.groupby(['origin', 'distcat'])


# In[184]:


nyc_Gr.distcat.count()


# In[185]:


nycf['discat2'] = pd.cut(nycf.distance, 3, labels=['Short', 'Medium', 'Long'])


# In[186]:


nycf.head()


# In[187]:


nycf.groupby('discat2').flight.count()


# In[188]:


nyc_sub = nycf[nycf['status'] == 'delayed']


# In[189]:


nyc_group = nyc_sub.groupby(['origin', 'discat2'])


# In[190]:


nyc_group.flight.count()


# In[ ]:




