import numpy as np

sales = [10, 20, 30, 40, 50, 60,
         70, 80, 90, 100, 110, 120]

arr = np.array(sales)

# Reshape into 4 rows and 3 columns
new_arr = arr.reshape(4, 3)

print("Reshaped array:")
print(new_arr)
