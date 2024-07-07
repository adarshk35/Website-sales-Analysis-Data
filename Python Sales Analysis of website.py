#!/usr/bin/env python
# coding: utf-8

# # For first time using Jupyter we need pip install

# In[6]:


get_ipython().system('pip install numpy')
get_ipython().system('pip install pandas')
get_ipython().system('pip install matplotlib')
get_ipython().system('pip install seaborn')


# In[8]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[12]:


df = pd.read_csv(r'C:\Users\Varsha\Downloads\Python_Diwali_Sales_Analysis\Python_Diwali_Sales_Analysis\Diwali Sales Data.csv', encoding= 'unicode_escape')
# to avoid encoding error, we use "unicode_escape"


# In[31]:


df.shape
# The error TypeError: 'tuple' object is not callable occurs because df.shape is an attribute, 
# not a method, and therefore should not be called with parentheses.


# In[16]:


df.head()


# In[152]:


df.info()


# # to delete the NaN values :
# 

# In[ ]:


df.drop(['Status', 'unnamed1'], axis=1, inplace=True)
# The "inplace=True" parameter is used in Pandas DataFrame methods to modify the DataFrame directly 
# rather than returning a modified copy.This can be useful for saving memory and writing more concise code.
## run it once only otherwise it will give the error.


# In[24]:


df.info()


# In[26]:


# to show if values are null or not:
pd.isnull(df)


# # to check whether any column has any null values:

# In[29]:


pd.isnull(df).sum()


# In[33]:


df.shape


# #  drop null values:

# In[37]:


df.dropna(inplace=True)


# In[39]:


df.shape


# # to change the datatype:
# 

# In[41]:


df['Amount']= df['Amount'].astype('int')


# In[44]:


df['Amount'].dtypes


# In[47]:


df.columns
# df.columns is an attribute not a method so we won't use (parenthesis)


# # rename column

# In[57]:


df.rename(columns= {'Marital_Status':'Married'}, inplace=True)


# In[59]:


df.describe()


# # describe specific columns

# In[62]:


df[['Orders', 'Age', 'Amount']].describe()


# # "Exploratory Data Analysis"
# 

# # Gender
# 

# In[154]:


cp = sns.countplot(data= df, x = 'Gender')
for bars in cp.containers:
    cp.bar_label(bars)
    
sns.set(rc={'figure.figsize':(3,3)})


# In[84]:


df.groupby(['Gender'], as_index=False )['Amount'].sum()


# In[157]:


sales_gender = df.groupby(['Gender'], as_index=False)['Amount'].sum()
sg=sns.barplot(data=sales_gender,x='Gender', y='Amount')
for bars in sg.containers:
    sg.bar_label(bars)

sns.set(rc={'figure.figsize':(3,5)})


# from the above graph we can see that most of the buyers are females and the purchasing power of females is more than males.
# The amount mentioned in (10^^7)

# In[101]:


ag= sns.countplot(data=df, x='Age Group', hue= 'Gender')
for bars in ag.containers:
    ag.bar_label(bars)


# ###### sales_by_age= df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount')
# 

# In[160]:


sns.barplot(data= sales_by_age, x='Age Group', y='Amount')

sns.set(rc={'figure.figsize':(10,3)})


# # orders by state

# In[126]:


Order_by_state= df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(12)
sns.set(rc={'figure.figsize':(20,7)})
sns.barplot(data= Order_by_state, x='State', y='Orders')


# In[128]:


Amount_by_state= df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(12)
sns.set(rc={'figure.figsize':(20,7)})
sns.barplot(data= Amount_by_state, x='State', y='Amount')


# The top 6 states are maintaining the same postion in orders as well as the amount, but from 7th to 11th position we see a shuffling in positions

# # On the basis of Marital Status 

# In[132]:


df.columns


# In[151]:


ms= sns.countplot(data=df, x='Married', hue='Gender')
sns.set(rc={'figure.figsize':(5,6)})
for bars in ms.containers:
    ms.bar_label(bars)


# In[172]:


Amount_spend= df.groupby(['Married', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(data= Amount_spend, x='Married', y='Amount', hue='Gender')
sns.set(rc={'figure.figsize':(5,6)})


# Here we can conclude that both the amount spend and the orders placed are more by women who are married.

# # On the basis of occupation:

# In[185]:


occ= sns.countplot(data=df, x='Occupation')
sns.set(rc={'figure.figsize':(25,9)})
for bars in occ.containers:
    occ.bar_label(bars)


# order by occupation

# In[190]:


Amount_spend= df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(data= Amount_spend, x='Occupation', y='Amount')
sns.set(rc={'figure.figsize':(25,9)})


# Amount spend by Occupation
From the above graphs we can say that the most orders palced and the amount spend are from people working in IT Sector, Healthcare nad Avaition sectors
# # On the basis of Product Categories:

# In[196]:


pc= sns.countplot(data=df, x='Product_Category')
sns.set(rc={'figure.figsize':(20,5)})
for bars in pc.containers:
    pc.bar_label(bars)


# Orders placed on the basis of Product Categories

# In[201]:


Amount_spend= df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.barplot(data= Amount_spend, x='Product_Category', y='Amount')
sns.set(rc={'figure.figsize':(20,6)})


# Amount spend on the basis of Product Categories

# # Insights:
# Although the number of orders are most in Clothing but the most amount spend is in Food.
# Variation in other categeries data as well like the the orders placed in Footwear, Electronic and Clothing are quite different but the amount spend on tehm is quite similar

# # On the basis  of product_ids:

# In[207]:


pc= sns.countplot(data=df, x='Product_ID')
sns.set(rc={'figure.figsize':(20,5)})
for bars in pc.containers:
    pc.bar_label(bars)


# In[221]:


p_id= df.groupby('Product_ID', as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.barplot(data=p_id, x='Product_ID', y='Amount')


# weightage of Amounts of Product__ID ordered 

# In[222]:


p_id= df.groupby('Product_ID', as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.barplot(data=p_id, x='Product_ID', y='Orders')

