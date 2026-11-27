import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Given data
salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])

departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]

# Convert into DataFrame
df = pd.DataFrame({
    "Salary": salaries,
    "Department": departments
})

print(df)


# 1. Line Graph - Salary Trend

plt.figure(figsize=(8, 5))

plt.plot(df.index, df["Salary"], marker='o')

plt.title("Employee Salary Trend")
plt.xlabel("Employee Index")
plt.ylabel("Salary")

plt.grid()
plt.show()


# 2. Bar Chart - Department-wise Salary Comparison

department_salary = df.groupby("Department")["Salary"].mean()

plt.figure(figsize=(8, 5))

plt.bar(department_salary.index, department_salary.values)

plt.title("Department-wise Average Salary")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.show()


# 3. Pie Chart - Department Distribution

department_count = df["Department"].value_counts()

plt.figure(figsize=(7, 7))

plt.pie(
    department_count,
    labels=department_count.index,
    autopct='%1.1f%%'
)

plt.title("Department Distribution")
plt.show()


# 4. Histogram - Salary Distribution

plt.figure(figsize=(8, 5))

plt.hist(salaries, bins=5, edgecolor='black')

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.show()


# 5. Scatter Plot - Index vs Salary

plt.figure(figsize=(8, 5))

plt.scatter(df.index, df["Salary"])

plt.title("Employee Index vs Salary")
plt.xlabel("Employee Index")
plt.ylabel("Salary")

plt.show()
