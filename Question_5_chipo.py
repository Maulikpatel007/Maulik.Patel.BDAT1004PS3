#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Step 1. Import the necessary libraries
import pandas as pd

# Step 2. Import the dataset from the provided address
url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"

# Step 3. Assign it to a variable called chipo.
chipo = pd.read_csv(url, sep='\t')

# Step 4. See the first 10 entries
print(chipo.head(10))

# Step 5.What is the number of observations in the dataset?
num_observations = chipo.shape[0]

# Step 6. What is the number of columns in the dataset?
num_columns = chipo.shape[1]

# Step 7. Print the name of all columns
print(chipo.columns)

# Step 8. How the dataset is indexed
print(chipo.index)

# Step 9. Which was the most-ordered item?
most_ordered_item = chipo['item_name'].value_counts().idxmax()

# Step 10.  For the most-ordered item, how many items were ordered?
most_ordered_item_count = chipo['item_name'].value_counts().max()

# Step 11. What was the most ordered item in the choice_description column?
most_ordered_choice = chipo['choice_description'].value_counts().idxmax()

# Step 12. How many items were orderd in total?
total_ordered_items = chipo['quantity'].sum()

# Step 13. Convert item price to a float
chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:]))

# Step 14. How much was the revenue for the period in the dataset?
revenue = (chipo['item_price'] * chipo['quantity']).sum()

# Step 15. How many orders were made in the period?
num_orders = chipo['order_id'].nunique()

# Step 16. What is the average revenue amount per order?
average_revenue_per_order = revenue / num_orders

# Step 17. How many different items are sold?
num_different_items = chipo['item_name'].nunique()

print("Number of observations:", num_observations)
print("Number of columns:", num_columns)
print("Most-ordered item:", most_ordered_item)
print("Number of the most-ordered item:", most_ordered_item_count)
print("Most ordered choice in choice_description:", most_ordered_choice)
print("Total ordered items:", total_ordered_items)
print("Revenue for the period:", revenue)
print("Number of orders:", num_orders)
print("Average revenue per order:", average_revenue_per_order)
print("Number of different items sold:", num_different_items)


# In[ ]:




