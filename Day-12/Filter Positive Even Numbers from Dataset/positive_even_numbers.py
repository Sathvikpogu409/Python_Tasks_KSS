import numpy as np

arr = np.array([-5, 10, 15, -2, 20, 25, 30])

# Filter positive even numbers
filtered = arr[(arr > 0) & (arr % 2 == 0)]

print("Positive even numbers:", filtered)
