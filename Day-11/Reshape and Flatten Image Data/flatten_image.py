import numpy as np

image = [[1, 2, 3],
         [4, 5, 6]]

# Convert into NumPy array
arr = np.array(image)

# Flatten into 1-D array
flat_arr = arr.flatten()

print("Original array:")
print(arr)

print("Flattened array:")
print(flat_arr)
