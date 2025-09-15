import pandas as pd

df = pd.read_csv("Employee.csv")
print(df.head())   # Show first 5 rows
print(df.info())   # Structure & data types
print(df.isnull().sum())  # Check for missing values

df = df.dropna()  # OR
df['column_name'].fillna(df['column_name'].mean(), inplace=True)