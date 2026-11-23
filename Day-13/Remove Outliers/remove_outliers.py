import numpy as np

values = np.array([10, 12, 15, 18, 100, 14, 13])

mean = np.mean(values)
std = np.std(values)

print("Mean:", mean)
print("Standard Deviation:", std)

filtered = values[np.abs(values - mean) <= 2 * std]

print("Data after removing outliers:", filtered)
