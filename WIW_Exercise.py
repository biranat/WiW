#!/usr/bin/env python
# coding: utf-8

# In[118]:


#Importing the required libraries
import pandas as pd
import requests
import string

#Downloading the datasets from repo and printing the download status: Successful or Unsuccessful
for char in string.ascii_lowercase:
    url = "https://public.wiwdata.com/engineering-challenge/data/"+str(char)+".csv"
    output_file = str(char)+".csv"
    print(output_file)
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_file, 'wb') as f:
            f.write(response.content)
        print("Download Successful: ",output_file)
    else:
        print("Download Unsuccessful!: ", output_file)
        
#Creating the paths list to upload data into dataframes
paths = []
for char in string.ascii_lowercase:
    path = "C:/Users/biran/Desktop/When I Work Challenge/"+str(char)+".csv"
    paths.append(path)
    print(path)
    
#Creating a dictionary of dataframes with uploaded data from source files
dfs = {}

for x, path in enumerate(paths, 1):
    df_name = f"df_{x}"
    print(df_name)
    dfs[df_name] = pd.read_csv(path)
    
#Pivoting the dataframes to get the necessary columns with correct information
#Then reindexing the dataframe and filling the NaN with 0 and changing the data type to int
#Then storing the new dataframes to new dictionary of dataframes called pivoted_dfs
pivoted_dfs = {}
for y, df in enumerate(dfs,1):
    pivoted_df = dfs[f'df_'+str(y)].pivot(index='user_id', columns='path', values='length') 
    pivoted_df = pivoted_df.reset_index()
    pivoted_df.fillna(0, inplace=True)
    pivoted_df = pivoted_df.astype(int)
    pivoted_dfs[f'df{y+1}_pivoted'] = pivoted_df
    print(f'df{y+1}_pivoted')

#Concatenated all the Dataframes into one final dataframe and exported the csv file
#Reason for choosing concatenation is all the files had unique IDs and same feature columns i.e. 14
concatenated_df = pd.concat(pivoted_dfs.values(), ignore_index = True)
concatenated_df.to_csv("Merged_file.csv", index=False) 
print('Script ran successfully, data download, pivot and merge is complete!')


# In[ ]:




