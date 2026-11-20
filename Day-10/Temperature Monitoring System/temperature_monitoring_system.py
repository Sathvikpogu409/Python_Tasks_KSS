#Temperature Monitoring System
#A weather station records temperatures for two days.
#Scenario:
#Day 1: [30, 32, 31]
#Day 2: [29, 33, 34]
#Task:
#● Create a 2D NumPy array to store this data.
#● Print the array.
#● Find the total temperature recorded. ,
#thes questions were about numpy, so giv answers based n that and
#give me folder name too

import numpy as np

# Store temperature data for two days
temperatures = np.array([
    [30, 32, 31],
    [29, 33, 34]
])

# Print the 2D array
print("Temperature Data:")
print(temperatures)

# Find total temperature
total = np.sum(temperatures)

print("Total Temperature:", total)
