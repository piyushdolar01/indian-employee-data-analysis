import pandas as pd
import numpy as np

df = pd.read_excel("D:\Indian_Employee_Data\Indian_Employee_Data.xlsx")
print(df)


print(df.head(10))
print(df.info())
print(df.describe())
print(df.columns.to_list())

print(df.isnull().sum())

print(df.shape())


# High Salary > 700000

high_salary = df[df["Salary"] > 700000]
print("Employee with salary > 700000")
print(high_salary)


# Salary > 700000 and Age >30

filtered_and = df[(df['Age'] > 30) & (df["Salary"] > 700000)]
print(f"Employee list Age > 30 + Salary > 700000")
print(filtered_and)

# Salary > 700000 and Age >30

filtered_or = df[(df['Age'] > 30) | (df["Salary"] > 700000)]
print(f"Employee list Age > 30 + Salary > 70000")
print(filtered_or)

# Updating

df.loc[1, 'Department'] = 'Data Analytics'
print(df)

df.iloc[1,4] = 'Data Scientist'
print(df)

# Increasing salary by 5%

df['Salary'] = df['Salary'] * 5/10
print(df)

# Save file

df.to_excel("Newdata.xlsx")

# Grouping 

grouped = df.groupby("Department")["Salary"].sum()
print(grouped)

grouped_multi = df.groupby(["Age", "Name"])["Salary"].sum()
print(grouped_multi)

# Sorting

df.sort_values(by="Age", ascending=True, inplace=True)
print(df)

df.sort_values(by=["Age","Salary"], ascending=[True,True], inplace=True)
print(df)

count_salary = df["Salary"].count()
print(count_salary)

avg_salary = df["Salary"].mean()
print(avg_salary)

# Missing data handle

df.dropna(inplace=True)
print(df)

df["Age"].fillna(df["Age"].mean(),inplace=True)
print(df)

df["Performance_Rating"].fillna(df["Performance_Rating"].mean(), inplace=True)
print(df)

# Interpolate method

df["Performance_Rating"] = df["Performance_Rating"].interpolate(method="linear")
print(df)