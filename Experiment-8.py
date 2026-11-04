import pandas as pd
df1=pd.DataFrame({
    'id':[1,2,3,4],
    'Name':["Aum","Sai","Ram","sita"],
    'marks':[85,90,78,88]
})
df2=pd.DataFrame({
    'id':[3,4,5,6],
    'Department':['CSE','ECE','EEE','MECH'],
    'city':['hyd','chennai','delhi','mumbai']
})
df3=pd.DataFrame({
   'id':[7,8],
   'Name':['easwer','gopal'],
   'Marks':[92,81]
})
print('Dataframe-1')
print(df1)
print('Dataframe-2')
print(df2)
print('Dataframe-3')
print(df3)
# merging 
inner_merge=pd.merge(df1,df2,on='id',how='inner')
print('inner_merge',inner_merge)
left_merge=pd.merge(df1,df2,on='id',how='left')
print('left_merge',left_merge)
right_merge=pd.merge(df1,df2,on='id',how='right')
print('right_merge',right_merge)
outer_merge=pd.merge(df1,df2,on='id',how='outer')
print('outer_merge',outer_merge)
print('-'*50)
contact_rows=pd.concat([df1,df3],ignore_index=True)
print('row',contact_rows)
print('-'*50)

contact_columns=pd.concat([df1,df2],axis=1)
print('column',contact_columns)
print('-'*50)
# handling missing values after merging
print('table-7',outer_merge)
filled_data=outer_merge.fillna('Not Available')
print('-'*50)
print(filled_data)
