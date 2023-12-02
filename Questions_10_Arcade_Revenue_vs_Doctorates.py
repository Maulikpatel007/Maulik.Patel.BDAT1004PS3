#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


# Load the dataset
data = pd.read_csv('arcade-revenue-vs-cs-doctorates.csv')


# In[4]:


# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(data['Total Arcade Revenue (billions)'], data['Computer Science Doctorates Awarded (US)'], c=data['Year'], cmap='viridis', s=100, edgecolors='black', alpha=0.8)
plt.xlabel('Total Arcade Revenue (billions)')
plt.ylabel('Computer Science Doctorates Awarded (US)')
plt.title('Relationship between Arcade Revenue and CS Doctorates (2000-2009)')
plt.colorbar(label='Year')
plt.grid(True)
plt.tight_layout()
plt.show()

