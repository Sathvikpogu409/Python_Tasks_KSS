#A user wants to save grocery items in a file grocery.txt. Write a Python program that 
#takes multiple items from the user and writes them into the file, with each item on a new line.

# Open the file in write mode
file = open("grocery.txt", "w")

# Get the number of grocery items
n = int(input("How many items do you want to enter? "))

# Get items from the user
for i in range(n):
    item = input("Enter grocery item: ")
    file.write(item + "\n")

# Close the file
file.close()

print("Grocery items saved successfully!")
