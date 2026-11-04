
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = {
        'maths': [78,85,96,80,86,90,70,88,92,75],
        'science': [84,79,95,78,88,91,72,85,94,74],
        'English': [75,82,90,76,85,89,68,84,91,73]
    }

df = pd.DataFrame(data)

print(df)

# Scatter plot: Maths vs Science
plt.figure(figsize=(6, 4))
plt.scatter(df['maths'], df['science'])
plt.title('Scatter Plot: Maths vs Science')
plt.xlabel('Maths Marks')
plt.ylabel('Science Marks')
plt.show()

# Correlation matrix
correlation = df.corr()

print('Correlation Matrix')
print(correlation)

# Correlation heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix Heatmap')
plt.show()

# Pair plot
pair = sns.pairplot(df)
pair.figure.suptitle('Pair Plot of Subject Marks', y=1.02)
plt.show()
sns.pairplot(df[['maths','science','English']])
plt.show()