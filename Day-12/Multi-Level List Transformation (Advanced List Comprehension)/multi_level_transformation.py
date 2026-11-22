data = [[1, 2, 3], [4, 5], [6]]

# Flatten the list
flat_list = [num for sublist in data for num in sublist]

# Find squares of even numbers
even_squares = [num ** 2 for num in flat_list if num % 2 == 0]

print("Flattened list:", flat_list)
print("Even number squares:", even_squares)
