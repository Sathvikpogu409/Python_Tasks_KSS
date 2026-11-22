import numpy as np

marks = [[78, 85],
         [90, 88],
         [67, 72]]

arr = np.array(marks)

# Access second student's second subject mark
print("Mark:", arr[1, 1])
