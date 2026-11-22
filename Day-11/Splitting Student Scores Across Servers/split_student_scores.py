import numpy as np

scores = [50, 60, 70, 80, 90, 100, 110, 120]

# Convert list into NumPy array
arr = np.array(scores)

# Split array into 4 equal parts
parts = np.array_split(arr, 4)

print("Split arrays:")
for part in parts:
    print(part)
