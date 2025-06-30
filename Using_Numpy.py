import numpy as np
import pandas as pd

df = pd.read_csv("D:\Indian_Employee_Data\Indian_Employee_Data_csv.csv")
print(df)

it_dept = df[df["Department"]=='IT']
print("Printed Department ")
print(it_dept)

high_salary = df[df["Salary"]> 700000]
print("Printed Salary ")
print(high_salary)

and_condition = df[(df["Gender"] == "Female") & (df["Department"] == "HR") & (df["Salary"]> 300000)]
print("Filtering with Multiple Conditions Using and")
print(and_condition)

or_condition = df[(df["Gender"] == "Male") | (df["Department"] == "IT") | (df["Salary"]> 700000)]
print("Filtering with Multiple Conditions Using or")
print(or_condition)

df.replace([np.inf, -np.inf], np.nan, inplace=True)
print(df)

df["Performance_Rating"] = pd.to_numeric(df["Performance_Rating"], errors="coerce")
df["Performance_Rating"].fillna(df["Performance_Rating"].mean(), inplace=True)
print(df)

missing_age = df[df["Age"].isnull()]
print(missing_age)

filter_row = df[(df["Projects_Completed"].isnull()) | (df["Projects_Completed"] == 0)]
print(filter_row)

emp_age = df[(df["Age"] >= 30) & (df["Age"] <= 35)]
print(emp_age)

Perfomance_rate = df[df["Performance_Rating"]> 4]
print(Perfomance_rate)

education = df[df["Education"].str.lower() == "b.tech"]
print(education)

startwith = df[df["Name"].str.startswith("A")]
print(startwith)

df["Joining_Date"] = pd.to_datetime(df["Joining_Date"], errors="coerce")
join_date = df[df["Joining_Date"] > "2020-01-01"]
print(join_date)

highest_paid = df.nlargest(5, "Salary")
print(highest_paid)

lowest_paid = df.nsmallest(5,"Salary")
print(lowest_paid)

df.to_csv("D:/Indian_Employee_Data/cleaned_employee_data.csv", index=False)
print("Cleaned data saved to cleaned_employee_data.csv")