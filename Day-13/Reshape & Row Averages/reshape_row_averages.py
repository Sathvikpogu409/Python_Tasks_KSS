import numpy as np

data = np.arange(1, 13)

matrix = data.reshape(3, 4)

print("3x4 Matrix:")
print(matrix)

row_average = np.mean(matrix, axis=1)

print("Average of Each Row:", row_average)
