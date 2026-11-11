# Import modules from Packages
from utilities import math_operations
from utilities import string_operations

# Mathematical operations
num1 = 10
num2 = 5

print("Addition:", math_operations.add(num1, num2))
print("Multiplication:", math_operations.multiply(num1, num2))

# String operations
text = "Python Programming"

print("Uppercase:", string_operations.uppercase(text))
print("Character count:", string_operations.count_characters(text))
