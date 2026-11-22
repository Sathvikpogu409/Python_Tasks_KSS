#A bank stores the transaction amounts of a customer in a list: 
#[1200, 500, 800, 1500] 
#Scenario: 
#● Convert the list into a NumPy array. 
#● Print the type of the object. 
#● Verify that it is a NumPy ndarray

import numpy as np

transactions = [1200, 500, 800, 1500]

# Convert list into NumPy array
arr = np.array(transactions)

# Print the array
print("Array:", arr)

# Print the type
print("Type:", type(arr))

# Verify NumPy ndarray
print("Is NumPy ndarray:", isinstance(arr, np.ndarray))
