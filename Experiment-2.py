import pandas as pd
import numpy as np
data={
    'Name':["Aum","Sai","Ram","sita","shiva","Narayana"],
    'Age':[20,25,18,15,25,20],
    'Marks':[100,90,75,80,77,50]
}
df=pd.DataFrame(data)
print("-"*5,"Dataset","-"*5)
print(df)
print('-'*10,"Data types"'-'*10,)
print(df.dtypes,)
print('--'*5,"checking missing valuse",'--'*5)
print('-'*10,"Checking null values",'-'*10,)
print(df.isnull())
print('-'*10,"sum of null values",'-'*10,)
print(df.isnull().sum())