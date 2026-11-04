import pandas as pd
data={
    'Name':["Aum","Sai","Ram","sita","shiva","Narayana"],
    'Age':[20,25,18,15,25,20],
    'Marks':[100,90,75,80,77,50],
    'department':['HR','IT','Finance','IT','HR','Finance'],
    "salary":[50000,45000,52000,48000,400000,80000],
}
df=pd.DataFrame(data)
print("original dataset")
print(df)
# grouping data using groupby
print(' average marks department wise')
group=df.groupby('department')['Marks'].mean()
print(group)
# multiple aggergate statistics
print('aggergate statistics for salary')
agg=df.groupby('department')['salary'].agg(['sum','mean','max','min'])
print(agg)
# grouping by multiple columns
print('average value based on dept and salary')
mult=df.groupby(['department','salary'])['Marks'].mean()
print(mult)
# pivot
print('pivot tables')
pivot=pd.pivot_table(df,values='Marks',index='department',columns='salary',aggfunc='mean')
print(pivot)
print('pivot tables with multiple aggregate')
pivot_salary=pd.pivot_table(df,values='salary',index='Age',columns='department',aggfunc=['mean','sum'])
print(pivot_salary)
