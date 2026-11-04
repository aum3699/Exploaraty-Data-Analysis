import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
data={
    "Age":[20,18,22,23,25],
    "salary":[20000,25000,30000,40000,50000],
    'department':['HR','IT','Finance','IT','HR'],
    'City':['hyderbad','chennai','Banglore','hyderbad','chennai']
}
df=pd.DataFrame(data)
print('original dataset')
print(df)
# normalization
minmax=MinMaxScaler()
df["Age_normalization"]=minmax.fit_transform(df[["Age"]])
print('After normalization')
print(df[['Age','Age_normalization']])
# standarization
standard=StandardScaler()
df['salary_Standardized']=standard.fit_transform(df[['salary']])
print('After standarization')
print(df[['salary','salary_Standardized']])
# log transformation
df['salary_log']=np.log(df['salary'])
print('after log transformation')
print(df[['salary','salary_log']])
# label encoding
label=LabelEncoder()
df['department_label']=label.fit_transform(df['department'])
print('after label encoding')
print(df[['department','department_label']])
# one hot encoding
one_hot=pd.get_dummies(df['City'])
print('after one-hot encoding')
print(one_hot)