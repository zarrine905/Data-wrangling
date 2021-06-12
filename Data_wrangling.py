#Read dataframe 
#If one cell empty in a row, then replace with mean of the other two values
#If two cells empty in a row, replace it with the value of third cell non-null value
#If three cells empty, drop the particular row
#Author: Zarrine
#Date: 12/062021

import pandas as pd
import numpy as np

df = pd.read_excel("input.xlsx")
df1 = df.dropna(axis=0,thresh=2)  # if three cells empty in a row

for i in range(len(df1)):
	#if two cells empty in a row
    if (np.isnan(df1.iloc[i,1])) and (np.isnan(df1.iloc[i,2])):
        df1.iloc[i,1] = df1.iloc[i,3] 
        df1.iloc[i,2] = df1.iloc[i,3]
        
    if (np.isnan(df1.iloc[i,2])) and (np.isnan(df1.iloc[i,3])):
        df1.iloc[i,2] = df1.iloc[i,1] 
        df1.iloc[i,3] = df1.iloc[i,1]
        
    if (np.isnan(df1.iloc[i,1])) and (np.isnan(df1.iloc[i,3])):
        df1.iloc[i,1] = df1.iloc[i,2] 
        df1.iloc[i,3] = df1.iloc[i,2]   
    
    #f one cell empty in a row
    if (np.isnan(df1.iloc[i,1])):
        df1.iloc[i,1] = (df1.iloc[i,2] + df1.iloc[i,3])/3
        
    if (np.isnan(df1.iloc[i,2])):
        df1.iloc[i,2] = (df1.iloc[i,1] + df1.iloc[i,3])/3
        
    if (np.isnan(df1.iloc[i,3])):
        df1.iloc[i,3] = (df1.iloc[i,1] + df1.iloc[i,2])/3
        
df1['A'] = df1['A'].round(decimals = 1)
df1['B'] = df1['B'].round(decimals = 1)
df1['C'] = df1['C'].round(decimals = 1)       
df1['D'] = df1["C"] - df1["A"]        
print(df1)
