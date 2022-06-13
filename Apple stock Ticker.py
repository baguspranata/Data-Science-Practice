#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install yfinance==0.1.67')


# In[2]:


import yfinance as yf
import pandas as pd


# In[3]:


apple = yf.Ticker("AAPL")


# In[6]:


apple_share_price_data = apple.history(period="max")


# In[7]:


apple_share_price_data.head()


# In[8]:


apple_share_price_data.reset_index(inplace=True)


# In[9]:


apple_share_price_data.plot(x="Date", y="Open")


# In[10]:


apple.dividends


# In[11]:


apple.dividends.plot()


# In[12]:


AMD = yf.Ticker("AMD")


# In[14]:


AMD_info=AMD.info
AMD_info


# In[16]:


AMD_info['country']


# In[25]:


AMD_info['sector']

