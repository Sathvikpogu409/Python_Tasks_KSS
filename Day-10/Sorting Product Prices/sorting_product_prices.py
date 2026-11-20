#Sorting Product Prices
#An e-commerce company stores product prices in a NumPy array.
#Scenario:
#Prices = [499, 299, 799, 199, 599]
#Task:
#● Convert it into a NumPy array.
#● Sort the prices in ascending order.


import numpy as np

# Store product prices
prices = [499, 299, 799, 199, 599]

# Convert list into NumPy array
arr = np.array(prices)

# Sort prices in ascending order
sorted_prices = np.sort(arr)

# Print sorted prices
print("Sorted Product Prices:", sorted_prices)
