import numpy as np

# Generate 3x3 random matrix
arr = np.random.randint(0, 51, (3, 3))

# Filter elements greater than 25
filtered = arr[arr > 25]

print("Random matrix:")
print(arr)

print("Values greater than 25:", filtered)
