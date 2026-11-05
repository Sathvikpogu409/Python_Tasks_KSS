def count_vowels(text):
    count = 0

    for i in text:
        if i in "aeiouAEIOU":
            count = count + 1

    return count


string = input("Enter a string: ")

result = count_vowels(string)

print("Number of vowels:", result)
