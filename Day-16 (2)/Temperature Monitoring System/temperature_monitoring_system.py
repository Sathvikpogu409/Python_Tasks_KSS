import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Given data
temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Create DataFrame
df = pd.DataFrame({
    "Day": days,
    "Temperature": temps
})

print(df)


# 1. Line Graph - Daily Temperature Trend

plt.figure(figsize=(8, 5))

plt.plot(df["Day"], df["Temperature"], marker='o')

plt.title("Daily Temperature Trend")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")

plt.grid()
plt.show()


# 2. Bar Chart - Day-wise Temperature

plt.figure(figsize=(8, 5))

plt.bar(df["Day"], df["Temperature"])

plt.title("Day-wise Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")

plt.show()


# 3. Pie Chart - High vs Low Temperature

high_temps = np.sum(temps > 30)
low_temps = np.sum(temps <= 30)

labels = ["High Temperature", "Low Temperature"]
values = [high_temps, low_temps]

plt.figure(figsize=(7, 7))

plt.pie(
    values,
    labels=labels,
    autopct='%1.1f%%'
)

plt.title("High vs Low Temperature")
plt.show()


# 4. Histogram - Temperature Frequency

plt.figure(figsize=(8, 5))

plt.hist(temps, bins=5, edgecolor='black')

plt.title("Temperature Frequency")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")

plt.show()


# 5. Scatter Plot - Day Index vs Temperature

plt.figure(figsize=(8, 5))

plt.scatter(range(len(temps)), temps)

plt.title("Day Index vs Temperature")
plt.xlabel("Day Index")
plt.ylabel("Temperature (°C)")

plt.show()
