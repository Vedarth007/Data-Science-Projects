# -*- coding: utf-8 -*-
"""data wrangling 2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12KqeOyfAZkM-4H8gXa14I3fkXIvuERkx
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv('student.csv')

df

df['Sem1']=df['Sem1'].fillna(df['Sem1'].mean())

df.isnull().sum()

df[df.isnull().any(axis=1)]

df

df['Sem1']=df['Sem1'].astype(int)

df

df['Sem2']=df['Sem2'].fillna(0)
df['Sem3']=df['Sem3'].fillna(0)
df['Sem4']=df['Sem4'].fillna(0)

df

df.boxplot()

plt.figure(figsize=(10, 6))
df.boxplot(column=['Sem1', 'Sem2', 'Sem3', 'Sem4', 'average Score'])
plt.title('Boxplot of Semester Scores')
plt.ylabel('Scores')
plt.xticks(rotation=45)
plt.show()

from scipy.stats.mstats import winsorize

# Winsorize the columns to remove outliers
cols = ['Sem1', 'Sem2', 'Sem3', 'Sem4', 'average Score']
for column in cols:
    df[column] = winsorize(df[column], limits=[0.05, 0.05])
plt.figure(figsize=(12, 6))
df[cols].boxplot()
plt.title("Boxplot of Numeric Columns after Winsorization")
plt.xticks(rotation=45)
plt.show()

df

# Calculate quartiles and IQR for each numeric column
Q1 = df[cols].quantile(0.25)
Q3 = df[cols].quantile(0.75)
IQR = Q3 - Q1

# Define upper and lower bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outliers
outliers = ((df[cols] < lower_bound) | (df[cols] > upper_bound)).any(axis=1)

# Remove outliers
df = df[~outliers]

# Visualize boxplots again to confirm outliers removal
plt.figure(figsize=(12, 6))
df[cols].boxplot()
plt.title("Boxplot of Numeric Columns after Removing Outliers using IQR")
plt.xticks(rotation=45)
plt.show()

import numpy as np

# Apply log transformation to 'average Score' variable
df['average Score'] = np.log1p(df['average Score'])

# Visualize the transformed variable
plt.figure(figsize=(8, 6))
plt.hist(df['average Score'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Transformed Average Score')
plt.xlabel('Transformed Average Score')
plt.ylabel('Frequency')
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Apply log transformation to 'average Score' variable
df['average Score'] = np.log1p(df['average Score'])

# Visualize the transformed variable
plt.figure(figsize=(8, 6))
plt.hist(df['average Score'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Transformed Average Score')
plt.xlabel('Transformed Average Score')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# define numerical & categorical columns
numeric_features = [feature for feature in df.columns if df[feature].dtype != 'O']
categorical_features = [feature for feature in df.columns if df[feature].dtype == 'O']

# print columns
print('We have {} numerical features : {}'.format(len(numeric_features), numeric_features))
print('\nWe have {} categorical features : {}'.format(len(categorical_features), categorical_features))
