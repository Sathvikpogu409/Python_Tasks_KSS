import numpy as np

# Original array
arr = np.array([10, 20, 30, 40])

# Create a copy
copy_arr = arr.copy()

# Modify original array
arr[0] = 100

print("Original array:", arr)
print("Copy array:", copy_arr)

# Create a new original array
arr2 = np.array([10, 20, 30, 40])

# Create a view
view_arr = arr2.view()

# Modify original array
arr2[0] = 100

print("Original array:", arr2)
print("View array:", view_arr)
