#!/usr/bin/env python
# coding: utf-8

# In the last few years, there have been multiple prison escapes where an inmate escapes by means of a helicopter. In this project, we will answer the following:
#     
# In which year did the most helicopter prison break attempts occur?

# # Import Modules
# 
# We begin by importing some helper fucntions.

# In[2]:


from helper import *


# # Get the Data
# 
# We will get the data from this wikipedia page: https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes.
# 
# Then we will print first 3 rows to analyse the data.

# In[3]:


url = "https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes"
data = data_from_url(url)
for row in data[:3]:
    print(row)


# # Removing the Details
# 
# Since the details column is not necessary for the project and taking lot of space, we will remove the column.
# 
# We initialize index variable with the value 0. Then use for loop to remove the Details column from every row.

# In[4]:


index = 0
for row in data:
    data[index]=row[:-1]
    index+=1
print(data)


# # Extracting the Year
# 
# In this step, we will iterate over data using iterable variable row. For every row, we will extract year from date. This is done to make it easier to analyse the data.

# In[5]:


for row in data:
    date = fetch_year(row[0])
    row[0] = date
print(data)


# # Attempts per Year
# 
# In this step, we will find the minimum and maximum years.

# In[6]:


min_year = min(data, key=lambda x: x[0])[0]
max_year = max(data, key=lambda x: x[0])[0]


# We need to make a list of years as we are calculating attempts per year. First we create an empty list names years. If the escape is attempted in a particular year between min_year & max_year, we will append it to the list by using for loop.  

# In[8]:


years = []
for year in range(min_year, max_year+1):
    years.append(year)
    
print(years)


# We will then create empty list for attempts per year. For every year in which escape was attempted we will append list [year, 0] to newly created list.

# In[9]:


attempts_per_year = []
for year in years:
    attempts_per_year.append([year, 0])


# In[10]:


print(attempts_per_year)


# And finally we increment the second entry (the one on index 1 which starts out as being 0) by 1 each time a year appears in the data.

# In[11]:


for row in data:
    for year_attempt in attempts_per_year:
        year = year_attempt[0]
        if row[0] == year:
            year_attempt[1]+=1
print(attempts_per_year)


# We will use matplotlib module to create bar chart to visualize attempts made for every year.

# In[12]:


get_ipython().run_line_magic('matplotlib', 'inline')
barplot(attempts_per_year)


# In[ ]:




