import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data={
    'Date':['2025-01-01','2025-02-01','2025-03-01','2025-04-01','2025-05-01','2025-06-01','2025-07-01','2025-08-01','2025-09-01','2025-10-01','2025-11-01','2025-12-01'],
    'sales':[120,135,150,170,165,180,210,220,200,190,175,160]
}
df=pd.DataFrame(data)
print(df)
df['Date']=pd.to_datetime(df['Date'])
print(df)
df.set_index('Date',inplace=True)
print(df)
plt.figure(figsize=(10,5))
plt.plot(df.index,df['sales'],marker='o')
plt.title('sales trend over time')
plt.xlabel('Date')
plt.ylabel('sales')
plt.grid(True)
plt.show()
df['Month']=df.index.month_name()
plt.figure(figsize=(10,5))
sns.barplot(x=df['Month'],y=df['sales'])
plt.title('monthly sales seasonality')
plt.xlabel('Month')
plt.ylabel('sales')
plt.xticks(rotation=45)
plt.show()