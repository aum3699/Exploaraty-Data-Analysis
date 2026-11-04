
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Marks': [45,56,67,78,89,90,56,73,68,92,81,77,85,69,58,64,72,88,95,49]
}

df = pd.DataFrame(data)

print('Dataset')
print(df)
print(df.describe())

# Histogram
plt.figure(figsize=(6, 4))
plt.hist(df['Marks'], bins=6)
plt.axvline(df['Marks'].mean(),linestyle='--', label='Mean')
plt.axvline(df['Marks'].median(),linestyle='--', label='Median')
plt.title('Histogram of Marks')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.legend()
plt.show()

# Boxplot
plt.figure(figsize=(6, 4))
plt.boxplot(df['Marks'])
plt.title('Boxplot of Marks')
plt.ylabel('Marks')
plt.show()

# Violin plot
plt.figure(figsize=(6, 4))
sns.violinplot(y=df['Marks'])
plt.title('Violin Plot of Marks')
plt.ylabel('Marks')
plt.show()
