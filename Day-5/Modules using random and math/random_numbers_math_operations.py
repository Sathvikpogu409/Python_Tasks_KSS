#Write a Python program that generates 20 random numbers between 1 and 200 using 
#the random module and store them in a list. 
#Then using the math module, compute and display: 
#● Maximum value 
#● Minimum value 
#● Square root of the maximum number 
#● Logarithm of the minimum number

import random
import math
numbers = []

for i in range(20):
    num = random.randint(1, 200)
    numbers.append(num)

maximum = max(numbers)
minimum = min(numbers)

square_root = math.sqrt(maximum)

log_value = math.log(minimum)

print("Random numbers:", numbers)
print("Maximum value:", maximum)
print("Minimum value:", minimum)
print("Square root of maximum:", square_root)
print("Logarithm of minimum:", log_value)
