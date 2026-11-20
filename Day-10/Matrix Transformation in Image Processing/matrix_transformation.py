#Matrix Transformation in Image Processing
#An image processing system stores pixel intensity values in a matrix.
#Scenario:
#[[1, 2],
#[3, 4]]
#Task:
#● Create a NumPy array for this matrix.
#● Find its transpose.
#● Print both matrices.

import numpy as np

# Create a 2D NumPy array
matrix = np.array([
    [1, 2],
    [3, 4]
])

# Find transpose of the matrix
transpose = np.transpose(matrix)

# Print both matrices
print("Original Matrix:")
print(matrix)

print("Transpose Matrix:")
print(transpose)
