#A list contains roll numbers: 
#[101, 102, 103, 104, 105, 106] 
#Scenario: 
#You want only the middle students (index 2 to 4). 



import numpy as np

roll_numbers = [101, 102, 103, 104, 105, 106]

arr = np.array(roll_numbers)

# Extract values from index 2 to 4
print("Middle students:", arr[2:5])
