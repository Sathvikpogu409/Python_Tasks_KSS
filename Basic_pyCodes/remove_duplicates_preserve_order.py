numbers = [1, 2, 3, 2, 4, 1, 5, 3]

result = []

for i in numbers:
    if i not in result:
        result.append(i)

print("List after removing duplicates:", result)
