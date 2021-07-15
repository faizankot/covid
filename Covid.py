#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime


# exploratory Data Analysis of Covid_19_India Dataset

# In[15]:


df=pd.read_csv("covid_19_india.csv")
df['Date'] = df['Date'].astype('datetime64[ns]')
df


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.info()

df.describe()
# Statewise Analysis

# In[7]:


df = df.groupby('State/UnionTerritory')['Confirmed','Cured','Deaths'].sum().reset_index()
df["Death_percentage"] = ((df["Deaths"] / df["Confirmed"]) * 100)
df.style.background_gradient(cmap='magma')


# In[8]:


px.bar(x=df.nlargest(10,"Confirmed")["State/UnionTerritory"],
       y = df.nlargest(10,"Confirmed")["Confirmed"],
       color_discrete_sequence=px.colors.diverging.Picnic,
       title="Top 10 states with highest number of Confirmed cases")


# In[9]:


px.bar(x=df.nlargest(10,"Cured")["State/UnionTerritory"],
       y = df.nlargest(10,"Cured")["Cured"],
       color_discrete_sequence=px.colors.sequential.Sunset,
       title="Top 10 states with highest number of Cured cases")


# In[10]:


px.bar(x=df.nlargest(10,"Deaths")["State/UnionTerritory"],
       y = df.nlargest(10,"Deaths")["Deaths"],
       color_discrete_sequence=px.colors.diverging.curl,
       title="Top 10 states with highest number of Deaths")


# In[11]:


px.bar(x=df.nlargest(10,"Death_percentage")["State/UnionTerritory"],
       y = df.nlargest(10,"Death_percentage")["Death_percentage"],
       color_discrete_sequence=px.colors.diverging.Portland,
       title="Top 10 states with highest of Death percentage")


# Monthwise Analysis

# In[17]:


month_wise = df.groupby(pd.Grouper(key='Date',freq='M')).sum()

month_wise = month_wise.drop(['Sno'], axis = 1)
month_wise['Date'] = month_wise.index

first_column = month_wise.pop('Date')
month_wise.insert(0, 'Date', first_column)

index = [x for x in range(len(month_wise))]
month_wise['index'] = index
month_wise = month_wise.set_index('index')

second_column = month_wise.pop('Confirmed')
month_wise.insert(1, 'Confirmed', second_column)
month_wise["Death_percentage"] = ((month_wise["Deaths"] / month_wise["Confirmed"]) * 100)
month_wise.style.background_gradient(cmap='twilight_shifted')


# In[18]:


fig = px.bar(month_wise, x='Date', y='Confirmed',
             hover_data=['Cured', 'Deaths'], color='Date',
             labels={'Date':'Date(monthwise)'},
             title="Monthwise Increase in Confirmed cases")
fig.show()


# In[19]:


fig = px.bar(month_wise, x='Date', y='Cured',
             hover_data=['Confirmed','Deaths'], color='Date',
             labels={'Date':'Date(monthwise)'},
             title="Monthwise Increase in Cured cases")
fig.show()


# In[20]:


fig = px.bar(month_wise, x='Date', y='Deaths',
             hover_data=['Confirmed','Cured'], color='Date',
             labels={'Date':'Date(monthwise)'},
             title="Monthwise Increase in Deaths cases")
fig.show()


# In[21]:


fig = px.bar(month_wise , 
             x='Date', 
             y='Death_percentage' ,
             hover_data=['Confirmed','Deaths'],color='Date',
             labels={'Death_percentage':'Death percentage'},
             title="Top 10 states with highest of Death percentage")
fig.show()


# Exploratory Data Analysis of StatewiseTestingDetails Dataset

# In[22]:


covid_testing = pd.read_csv("StatewiseTestingDetails.csv")
covid_testing['Date'] = covid_testing['Date'].astype('datetime64[ns]')
covid_testing.head()


# In[24]:


covid_testing.shape


# In[25]:


covid_testing.info()


# In[26]:


covid_testing.describe()


# In[27]:


covid_testing['Negative'] = covid_testing['TotalSamples'] - covid_testing['Positive']
covid_testing = covid_testing.dropna()
covid_testing.info()


# Statewise Analysis

# In[28]:


covid_testing_state = covid_testing.groupby('State')['TotalSamples','Negative','Positive'].max().reset_index()
covid_testing_state["Positive_percentage"] = ((covid_testing["Positive"] / covid_testing["TotalSamples"]) * 100)
covid_testing_state.style.background_gradient(cmap='gist_earth_r')


# In[29]:


px.bar(x=covid_testing_state.nlargest(10,"TotalSamples")["State"],
       y = covid_testing_state.nlargest(10,"TotalSamples")["TotalSamples"],
       labels={'y':'Total Samples','x':'State'},
       color_discrete_sequence=px.colors.sequential.haline,
       title="Top 10 states with highest number of Total Samples")


# In[30]:


px.bar(x=covid_testing_state.nlargest(10,"Negative")["State"],
       y = covid_testing_state.nlargest(10,"Negative")["Negative"],
       labels={'y':'Total Negative cases','x':'State'},
       color_discrete_sequence=px.colors.sequential.turbid,
       title="Top 10 states with highest number of Negative cases")


# In[31]:


px.bar(x=covid_testing_state.nlargest(10,"Positive")["State"],
       y = covid_testing_state.nlargest(10,"Positive")["Positive"],
       labels={'y':'Total Positive Cases','x':'State'},
       color_discrete_sequence=px.colors.sequential.solar,
       title="Top 10 states with highest number of Positive cases")


# In[32]:


px.bar(x=covid_testing_state.nlargest(10,"Positive_percentage")["State"],
       y = covid_testing_state.nlargest(10,"Positive_percentage")["Positive_percentage"],
       labels={'y':'Positive Percentage','x':'State'},
       color_discrete_sequence=px.colors.sequential.Aggrnyl,
       title="Top 10 states with highest Positive percentage",
       height = 420)


# In[ ]:




