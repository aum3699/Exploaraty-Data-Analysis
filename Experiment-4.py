import pandas as pd
import numpy as np
from scipy.stats import zscore
data={
    'Name':["Aum","Sai","Ram","sita","shiva","Aum"],
    'Marks':[100,90,75,80,77,500]
}
df=pd.DataFrame(data)
print(df)
# dublicates
print(df[df.duplicated()])
# drop duplicates
df_no_duplicates=df.drop_duplicates()
print("After Removing Dupilcates")
print(df_no_duplicates)
# detecting outliers using Z-score method
df_no_duplicates["Z_score"]=zscore(df_no_duplicates["Marks"])
print("-"*10,"Z-score method",'-'*10)
print(df_no_duplicates)
outliers=df_no_duplicates[
    (df_no_duplicates["Z_score"]>2) |
    (df_no_duplicates["Z_score"]<-2) 
]
print("-"*10,"Detect outliers",'-'*10)
print(outliers)
# removing outilers
cleaned_data=df_no_duplicates[
    (df_no_duplicates["Z_score"]<=2) &
    (df_no_duplicates["Z_score"]>=-2) 
]
print("-"*10,"Data after removing outliers",'-'*10)
print(cleaned_data)
# comparison
print("Before removing outilers")
print(df_no_duplicates["Marks"].describe())
print("After removing outilers")
print(cleaned_data["Marks"].describe())
