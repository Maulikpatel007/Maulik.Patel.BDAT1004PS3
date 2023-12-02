#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Step 1. Import the necessary libraries
import pandas as pd


# In[2]:


# Step 2. Import the dataset
url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user"
# Step 3. Assigning it to a variable called users
users = pd.read_csv(url, sep='|')


# In[3]:


# Step 4. Discover what is the mean age per occupation
mean_age_per_occ = users.groupby('occupation')['age'].mean()


# In[4]:


# Step 5. Discover the Male ratio per occupation and sort it from the most to the least 
users['is_male'] = (users['gender'] == 'M')
male_ratio_per_occ = users.groupby('occupation')['is_male'].mean().sort_values(ascending=False)


# In[5]:


# Step 6. For each occupation, calculate the minimum and maximum ages
min_max_age_per_occ = users.groupby('occupation')['age'].agg(['min', 'max'])


# In[6]:


# Step 7. For each combination of occupation and sex, calculate the mean age 
mean_age_per_combo = users.groupby(['occupation', 'gender'])['age'].mean()


# In[7]:


# Step 8. For each occupation present the percentage of women and men
gender_percent_per_occ = users.groupby(['occupation', 'gender'])['is_male'].count() / users.groupby('occupation')['is_male'].count() * 100


# In[8]:


print("Mean age per occupation:\n", mean_age_per_occ)
print("\nMale ratio per occupation (most to least):\n", male_ratio_per_occ)
print("\nMinimum and maximum ages per occupation:\n", min_max_age_per_occ)
print("\nMean age per combination of occupation and sex:\n", mean_age_per_combo)
print("\nPercentage of women and men per occupation:\n", gender_percent_per_occ)


# In[ ]:




