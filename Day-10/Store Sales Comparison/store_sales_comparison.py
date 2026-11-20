#Store Sales Comparison
#Two stores record daily sales for 3 days.
#Scenario:
#Store A = [200, 250, 300]
#Store B = [180, 270, 310]
#Task:
#● Store them in NumPy arrays.
#● Find the daily difference in sales between the two stores.
#● Print the resulting array.

import numpy as np

# Store daily sales
store_a = np.array([200, 250, 300])
store_b = np.array([180, 270, 310])

# Find daily difference in sales
difference = store_a - store_b

# Print the resulting array
print("Daily Sales Difference:", difference)
