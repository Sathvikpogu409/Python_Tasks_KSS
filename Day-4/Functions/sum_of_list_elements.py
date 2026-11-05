def find_sum(numbers):
    total = 0

    for i in numbers:
        total = total + i

    return total


numbers = [10, 20, 30, 40, 50]

result = find_sum(numbers)

print("Sum of list elements:", result)
