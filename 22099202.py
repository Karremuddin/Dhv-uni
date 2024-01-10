#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


# Load the dataset
file_path = 'air_pollution_dataset.csv'
data = pd.read_csv(file_path)


# In[4]:


print(data.head())  # Display the first few rows


# In[5]:


print(data.info())  # Display data types and missing values


# In[6]:


# Summary statistics 
print(data.describe())


# In[7]:


# Distribution plot for PM2.5 and PM10
plt.figure(figsize=(10, 6))
sns.histplot(data['PM2.5'], kde=True, color='blue', label='PM2.5')
sns.histplot(data['PM10'], kde=True, color='red', label='PM10')
plt.title('Distribution of PM2.5 and PM10')
plt.xlabel('Value')
plt.legend()
plt.show()


# # DASHBOARD

# In[16]:


fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Plot 1: Distribution of PM2.5 and PM10 (Histogram)
sns.histplot(data['PM2.5'], kde=True, color='blue', ax=axs[0, 0])
axs[0, 0].set_title('Distribution of PM2.5')
axs[0, 0].set_xlabel('PM2.5')
axs[0, 0].set_ylabel('Frequency')
axs[0, 0].grid(True)

# Plot 2: Country-wise Distribution of CO Levels (Pie Plot)
co_mean_by_country = data.groupby('Country')['CO'].mean().sort_values(ascending=False).head(10)
axs[0, 1].pie(co_mean_by_country, labels=co_mean_by_country.index, autopct='%1.1f%%', startangle=90)
axs[0, 1].set_title('Top 10 Countries by CO Levels')
axs[0, 1].grid(True)


# Plot 3: SO2 Distribution by City (Line Plot)
sns.lineplot(x='City', y='SO2', data=data.sort_values(by='SO2', ascending=False).head(10), color='green', marker='o', ax=axs[1, 0])
axs[1, 0].set_title('Top 10 Cities with Highest SO2 Levels')
axs[1, 0].set_xlabel('City')
axs[1, 0].set_ylabel('SO2 Level')
axs[1, 0].tick_params(axis='x', rotation=45)
axs[1, 0].grid(True)

# Plot 4: Distribution of NO2 (Histogram)
sns.histplot(data['NO2'], kde=True, color='orange', ax=axs[1, 1])
axs[1, 1].set_title('Distribution of NO2')
axs[1, 1].set_xlabel('NO2')
axs[1, 1].set_ylabel('Frequency')
axs[1, 1].grid(True)

# Create a new figure for the description
fig_desc = plt.figure(figsize=(12, 3))
plt.text(0, 0, "Figure Descriptions:\n\nDistribution of PM2.5 :\n"\
         "Shows the distribution of PM2.5 levels across the dataset.\n\n"\
         "Top 10 Countries by CO Levels :\n"\
         "Illustrates the proportion of CO levels in the top 10 countries with the highest average CO levels.\n\n"\
         "Top 10 Cities with Highest SO2 Levels :\n"\
         "Shows the top 10 cities with the highest SO2 levels.\n\n"\
         "Distribution of NO2 :\n"\
         "Displays the distribution of NO2 levels in the dataset.\n\n"\
         "Name - kareemuddin shaik.\n"\
         "Student id - 22099202", 
         ha='left', va='center', fontsize=14, wrap=True)
plt.axis('off')

fig.suptitle('Air Pollution Analysis', fontsize=16)
fig.tight_layout(rect=[0, 0.03, 1, 0.95])
# Save the dashboard as an image
plt.savefig('air_pollution.png', dpi=300, bbox_inches='tight')  # Save with adjusted bounding box
plt.show()


# In[ ]:




