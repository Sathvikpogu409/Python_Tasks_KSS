import numpy as np

temps = np.array([28, 32, 35, 31, 29, 40, 38])

filtered = np.where(temps > 30)

print("Temperatures above 30:", temps[filtered])
print("Day Indices:", filtered[0])
