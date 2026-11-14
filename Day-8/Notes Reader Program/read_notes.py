#A student stores daily notes in a file called notes.txt. Write a program that opens the 
#file, reads all the contents, and displays them on the screen.



# Open the file in read mode
file = open("notes.txt", "r")

# Read and display all contents
content = file.read()

print("Daily Notes:")
print(content)

# Close the file
file.close()
