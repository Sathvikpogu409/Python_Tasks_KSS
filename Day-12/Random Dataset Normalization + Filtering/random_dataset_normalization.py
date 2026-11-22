import numpy as np

# Generate 8 random float values
arr = np.random.rand(8)

# Normalize by multiplying by 100
normalized = arr * 100

# Filter values greater than 50
filtered = normalized[normalized > 50]

# Sort filtered values
sorted_values = np.sort(filtered)

print("Original array:", arr)
print("Normalized array:", normalized)
print("Filtered values:", filtered)
print("Sorted values:", sorted_values)
