import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Given data
sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]

# Create DataFrame
df = pd.DataFrame({
    "Product": products,
    "Sales": sales,
    "Profit": profit
})

print(df)


# 1. Line Graph - Sales Trend

plt.figure(figsize=(8, 5))

plt.plot(df["Product"], df["Sales"], marker='o')

plt.title("Product Sales Trend")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.grid()
plt.show()


# 2. Bar Chart - Product vs Sales

plt.figure(figsize=(8, 5))

plt.bar(df["Product"], df["Sales"])

plt.title("Product-wise Sales Comparison")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.show()


# 3. Pie Chart - Sales Contribution

plt.figure(figsize=(7, 7))

plt.pie(
    df["Sales"],
    labels=df["Product"],
    autopct='%1.1f%%'
)

plt.title("Product Sales Contribution")
plt.show()


# 4. Histogram - Profit Distribution

plt.figure(figsize=(8, 5))

plt.hist(df["Profit"], bins=5, edgecolor='black')

plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")

plt.show()


# 5. Scatter Plot - Sales vs Profit

plt.figure(figsize=(8, 5))

plt.scatter(df["Sales"], df["Profit"])

plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")

plt.grid()
plt.show()
