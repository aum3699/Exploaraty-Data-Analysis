import pandas as pd
data={
    'Name':["Aum","Sai","Ram","sita","shiva","Narayana"],
    'Age':[20,25,18,15,20,20],
    'Marks':[100,90,75,81,77,50],
}
df=pd.DataFrame(data)
print('original dataframe')
print('select name and marks')
print(df[['Name','Marks']])
print('specific row with index 2')
print(df.loc[2])
print('slicing rows from 0 to 4')
print(df[1:4])
print('students with marks greater than 80')
print(df[df['Marks'] > 80])

print('age 20 greater than 20 and marks greater than 80')
print(df[(df['Age'] == 20) & (df['Marks'] > 80)])

print('advance slicing using loc')
print(df.loc[:2, ['Name','Marks']])

print('advance slicing using iloc')
print(df.iloc[1:3,:2])