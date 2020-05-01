#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd


# In[22]:


data = pd.read_csv('./Data/train.csv')


# In[23]:


data.iloc[0:8]


# In[24]:


data.loc[:,['Name', 'Age']]


# In[25]:


data.loc[data['Name'] == 'Braund, Mr. Oven Harris']


# In[26]:


print(data.groupby(['Sex', 'Survived'])['PassengerId'].count())


# In[27]:


data.drop(data.columns[[3]], axis=1, inplace=True)


# In[28]:


data.drop(data.columns[[0]], axis=1, inplace=True)


# In[29]:


data.head()


# In[30]:


data.columns


# In[33]:


data.shape


# In[34]:


data = data[['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare',
       'Cabin']]
data.head()


# In[35]:


data.shape


# In[36]:


data.info()


# In[37]:


data = data[['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch']]
data.head()


# In[38]:


data['Age'].fillna(data['Age'].mean(), inplace=True)


# In[39]:


data.head()


# In[41]:


data['Sex'] = data['Sex'].map({'male': 0, 'female':1})


# In[42]:


data.head()


# In[43]:


data.to_csv('cleansed_csv', sep=',')


# In[44]:


data = data.dropna()


# In[46]:


x= data.drop('Survived', axis=1) 
y = data['Survived']


# In[49]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,random_state=1)


# In[50]:


from sklearn.svm import SVC
model = SVC(kernel='linear', probability=True, random_state=0)


# In[51]:


model.fit(x_train,y_train)


# In[52]:


y_predict = model.predict(x_test)
from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_predict)


# In[ ]:




