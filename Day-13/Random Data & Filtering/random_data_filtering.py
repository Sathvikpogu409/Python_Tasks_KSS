import numpy as np

nums = np.random.randint(1, 100, 10)

filtered = nums[nums % 5 == 0]

result = np.sort(filtered)

print("Random Numbers:", nums)
print("Divisible by 5:", filtered)
print("Sorted Result:", result)
