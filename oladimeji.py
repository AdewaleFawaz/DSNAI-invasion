#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
#initialize list of lists 
data= [['Ayo', 10], ['imran', 15], ['chucks', 14]]
#Creat the pandas DataFrame from the list and adding column headers  

df = pd.DataFrame(data, columns = ['Name', 'Age'])
# print DataFrame
df


# In[2]:


data= {'Name' : ['Ayo', 'imran','chucks'],'Age' :[10,15, 14]}
df=pd.DataFrame(data)
df


# In[3]:


dict_data = {"State": ["Abia", "Adamawa", "Lagos", "Osun", "Rivers"],
            "Capital": [" Umuahia" ,"Yola" , "Ikeja" , "Osogbo", "Portharcourt"],
            "area": [6320, 36917,3445,9251,11077],
            "population": [2845380, 3178950, 9113605, 3416959, 5198605]}
df= pd.DataFrame(dict_data)
df


# In[4]:


csv_df= pd.read_csv('Desktop/FAWAZ.csv')
print(csv_df)


# In[5]:



csv_df.describe()


# In[6]:


csv_df["POPULATION"].mean()


# In[7]:


csv_df["POPULATION"].std()


# In[8]:


csv_df["POPULATION"].sum()


# In[9]:


csv_df["POPULATION"].count()


# In[10]:


csv_df["POPULATION"].max()


# In[11]:


csv_df["POPULATION"].min()


# In[12]:


csv_df.info()                                


# In[13]:


csv_df.columns


# In[14]:


print(csv_df['STATES'])


# In[15]:


print(csv_df[['STATES']])


# In[16]:


print(csv_df[['STATES','POPULATION']])


# In[17]:


print(csv_df[0:4],"\n")


# In[18]:


print(csv_df[4:6])


# In[19]:


print(csv_df[0:11])


# In[20]:


print(csv_df.iloc[2])


# In[21]:


print(csv_df.iloc[3:5])


# In[22]:


df = csv_df.drop(["POPULATION"], axis = 1)
print(df)


# In[23]:


df["AREAS(KM2)"] =df["AREAS(KM2)"].astype("float")
df


# In[24]:


pd.to_numeric(df["AREAS(KM2)"],downcast='integer')


# In[26]:


df = csv_df.append(["POPULATION"])
print(csv_df)


# In[ ]:




