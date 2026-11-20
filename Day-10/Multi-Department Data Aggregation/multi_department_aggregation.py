#Multi-Department Data Aggregation
#A company collects employee counts from two branches.
#Branch A:
#[[10, 20],
#[30, 40]]
#Branch B:
#[[5, 15],
#[25, 35]]
#Scenario:
#● Combine the two matrices.
#● Calculate the total employees across all departments.
#● Print the combined matrix and total.


import numpy as np

# Create Branch A matrix
branch_a = np.array([
    [10, 20],
    [30, 40]
])

# Create Branch B matrix
branch_b = np.array([
    [5, 15],
    [25, 35]
])

# Combine both matrices
combined = np.concatenate((branch_a, branch_b))

# Calculate total employees
total = np.sum(combined)

# Print combined matrix and total
print("Combined Matrix:")
print(combined)

print("Total Employees:", total)
