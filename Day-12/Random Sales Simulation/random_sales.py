import numpy as np

# Generate 10 random sales values
sales = np.random.randint(100, 501, 10)

# Calculate average sales
average = np.mean(sales)

print("Daily sales:", sales)
print("Average sales:", average)
