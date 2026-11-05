text = input("Enter a string: ")

result = ""

for i in text:
    if i not in result:
        result = result + i

print("String after removing duplicates:", result)
