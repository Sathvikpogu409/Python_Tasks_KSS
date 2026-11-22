import numpy as np

prices = [10.5, 20.8, 15.3]

arr = np.array(prices)

# Convert float to integer
new_arr = arr.astype(int)

print("Original array:", arr)
print("Integer array:", new_arr)
