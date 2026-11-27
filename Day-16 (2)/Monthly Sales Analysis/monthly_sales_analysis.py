
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sales data
sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

# 1. Create DataFrame
df = pd.DataFrame({
    "Month": months,
    "Sales": sales
})

print(df)

# 2. Create Dashboard
plt.figure(figsize=(12, 10))

# Line Graph - Sales Trend
plt.subplot(3, 2, 1)
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid()

# Bar Chart - Month-wise Comparison
plt.subplot(3, 2, 2)
plt.bar(months, sales)
plt.title("Month-wise Sales Comparison")
plt.xlabel("Months")
plt.ylabel("Sales")

# Pie Chart - Monthly Contribution
plt.subplot(3, 2, 3)
plt.pie(sales, labels=months, autopct="%1.1f%%")
plt.title("Monthly Sales Contribution")

# Histogram - Frequency of Sales
plt.subplot(3, 2, 4)
plt.hist(sales, bins=5, edgecolor='black')
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")

# Scatter Plot - Index vs Sales
plt.subplot(3, 2, 5)
plt.scatter(range(len(sales)), sales)
plt.title("Month Index vs Sales")
plt.xlabel("Month Index")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()
