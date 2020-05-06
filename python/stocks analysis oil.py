#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import datetime
from pandas_datareader import data, wb
from pandas import Series, DataFrame


start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2020, 5, 6)

df = data.DataReader("ONGC.NS", 'yahoo', start, end)
df.tail()


# In[7]:


df_Y = data.DataReader("WIPRO.NS", 'yahoo', start, end)
df_Y.tail()


# In[8]:


close_px = df_Y['Adj Close']
mavg = close_px.rolling(window=100).mean()


# In[9]:


close_px


# In[10]:


get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
from matplotlib import style

# Adjusting the size of matplotlib
import matplotlib as mpl
mpl.rc('figure', figsize=(8, 7))
mpl.__version__

# Adjusting the style of matplotlib
style.use('ggplot')

close_px.plot(label='ONGC.NS')
mavg.plot(label='mavg')
plt.legend()


# In[11]:


df_GAIL = data.DataReader("GAIL.NS", 'yahoo', start, end)
close_px_GAIL = df_GAIL['Adj Close']
mavg_GAIL = close_px_GAIL.rolling(window=100).mean()

get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
from matplotlib import style

# Adjusting the size of matplotlib
import matplotlib as mpl
mpl.rc('figure', figsize=(8, 7))
mpl.__version__

# Adjusting the style of matplotlib
style.use('ggplot')

close_px_GAIL.plot(label='GAIL.NS')
mavg_GAIL.plot(label='mavg')
plt.legend()


# In[12]:


rets = close_px / close_px.shift(1) - 1
rets.plot(label='return')


# In[13]:


Rets_close_px_GAIL = close_px_GAIL / close_px_GAIL.shift(1) - 1
Rets_close_px_GAIL.plot(label='return')


# In[14]:


dfcomp = data.DataReader(['ONGC.NS', 'IOC.NS', 'HINDPETRO.NS', 'BPCL.NS', 'GAIL.NS', 'RELIANCE.NS', 'ADANIGAS.NS'],
                        'yahoo',start=start,end=end)['Adj Close']







# In[15]:


dfcomp.tail()


# In[16]:


retscomp = dfcomp.pct_change()

corr = retscomp.corr()


# In[17]:


corr


# In[18]:


retscomp.tail()


# In[19]:


plt.scatter(retscomp['ONGC.NS'], retscomp['GAIL.NS'])
plt.xlabel('Returns ONGC.NS')
plt.ylabel('Returns GAIL.NS')


# In[ ]:





# In[22]:


# pd.scatter_matrix(retscomp, diagonal='kde', figsize=(10, 10));


# In[23]:


plt.imshow(corr, cmap='hot', interpolation='none')
plt.colorbar()
plt.xticks(range(len(corr)), corr.columns)
plt.yticks(range(len(corr)), corr.columns);


# In[24]:


plt.scatter(retscomp.mean(), retscomp.std())
plt.xlabel('Expected returns')
plt.ylabel('Risk')
for label, x, y in zip(retscomp.columns, retscomp.mean(), retscomp.std()):
    plt.annotate(
        label, 
        xy = (x, y), xytext = (20, -20),
        textcoords = 'offset points', ha = 'right', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))


# In[ ]:




