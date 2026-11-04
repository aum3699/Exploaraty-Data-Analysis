import pandas as pd
import numpy as np
data={
    'Name':["Aum","Sai","Ram",np.nan,"shiva","Aum"],
    'Age':[20,25,np.nan,15,np.nan,20],
    'Marks':[100,90,np.nan,80,35,np.nan]
}
df=pd.DataFrame(data)
print("original dataset")
print("-"*10,"original dataset","-"*10)
print(df)
# mean 
print("-"*10,"Mean","-"*10)
mean=df.copy()
mean["Age"]=mean["Age"].fillna(mean["Age"].mean())
mean["Marks"]=mean["Marks"].fillna(mean["Marks"].mean())
print(mean.to_string())
# median
print("-"*10,"Median","-"*10)
median=df.copy()
median["Age"]=median["Age"].fillna(median["Age"].median())
median["Marks"]=median["Marks"].fillna(median["Marks"].median())
print(median.to_string())
#mode
print("-"*10,"Mode","-"*10)
mode=df.copy()
mode["Age"]=mode["Age"].fillna(mode["Age"].mode()[0])
mode["Marks"]=mode["Marks"].fillna(mode["Marks"].mode()[0])
mode["Name"]=mode["Name"].fillna(mode["Name"].mode()[0])
print(mode.to_string())
# frrward fill
print('-'*10,"Forward fill","-"*10)
forward_fill=df.ffill()
print(forward_fill)
# Backward fill
print('-'*10,"Backward fill","-"*10)
forward_fill=df.bfill()
print(forward_fill)
# Drop rows 
print("-"*10,"Drop rows","-"*10)
drop_rows=df.dropna()
print(drop_rows)
# Drop columns 
print("-"*10,"Drop columns","-"*10)
drop_columns=df.dropna(axis=1)
print(drop_columns)