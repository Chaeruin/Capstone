#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd


# In[12]:


df1= pd.read_csv('date.csv')#date_time.csv파일 불러오기


# In[62]:


df1_s = df1.sort_values(by=["temperature", "humidity"], ascending=[False, False]) 
#temperature, humidity열 내림차순 동시정렬


# In[24]:


df2 = pd.read_csv('tnh.csv')#tnh.csv파일 불러오기


# In[27]:


df2_s = df2.sort_values(by=["temperature", "humidity"], ascending=[False, False])
#temperature, humidity열 내림차순 동시정렬


# In[31]:


df3 = pd.read_csv('stay_time.csv')


# In[34]:


df3_s = df3.sort_values(by=["stay_time"], ascending=[False])


# In[43]:


df1.drop(df1.index[300:755], inplace=True)


# In[64]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[1]:


df3_s.info()


