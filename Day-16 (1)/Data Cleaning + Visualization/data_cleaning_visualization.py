import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Original data
data = np.array([100, np.nan, 200, 150, np.nan, 300])

# 1. Convert into Pandas Series
s = pd.Series(data)

# 2. Replace NaN with mean
mean_value = s.mean()
s = s.fillna(mean_value)

print("Cleaned Data:")
print(s)

print("Mean:", mean_value)

# 3. Line graph of cleaned data
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(s, marker='o')
plt.title("Line Graph")
plt.xlabel("Index")
plt.ylabel("Values")
plt.grid()

# 4. Bar chart of values > average
above_avg = s[s > mean_value]

plt.subplot(1, 2, 2)
plt.bar(above_avg.index, above_avg.values)
plt.title("Values Above Average")
plt.xlabel("Index")
plt.ylabel("Values")

plt.tight_layout()
plt.show()
