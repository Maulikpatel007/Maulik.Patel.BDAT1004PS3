#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Step 1. Import the necessary libraries
import pandas as pd
import numpy as np


# In[3]:


# Step 2. Create Series
series_1 = pd.Series(np.random.randint(1, 5, size=100))
series_2 = pd.Series(np.random.randint(1, 4, size=100))
series_3 = pd.Series(np.random.randint(10000, 30001, size=100))


# In[4]:


# Step 3. Create DataFrame by joining the Series by column
data = {'bedrs': series_1, 'bathrs': series_2, 'price_sqr_meter': series_3}
df = pd.DataFrame(data)


# In[5]:


# Step 4. Change column names
df.columns = ['bedrs', 'bathrs', 'price_sqr_meter']


# In[6]:


# Step 5. Create a one column DataFrame
bigcolumn = pd.DataFrame(pd.concat([series_1, series_2, series_3], axis=0))


# In[7]:


# Step 6. Check if 'bigcolumn' goes only until index 99
print("Is it true that 'bigcolumn' goes only until index 99:", bigcolumn.index.max() == 99)


# In[8]:


# Step 7. Reindex the DataFrame so it goes from 0 to 299
bigcolumn.reset_index(drop=True, inplace=True)
bigcolumn.index = range(300)


# In[9]:


# Print the resulting DataFrame
print(bigcolumn)

