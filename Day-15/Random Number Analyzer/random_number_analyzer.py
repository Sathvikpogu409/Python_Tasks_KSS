import random

numbers = []

for i in range(10):
    num = random.randint(1, 100)
    numbers.append(num)

print("Random Numbers:", numbers)

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)

unique_numbers = set(numbers)

print("Numbers without duplicates:", unique_numbers)
