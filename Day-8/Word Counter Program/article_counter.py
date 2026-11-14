#A writer saves an article in a file called article.txt. Write a Python program that: 
#● Opens and reads the file 
#● Counts the number of words, lines, and characters in the file 
#● Displays the results.


# Open the file in read mode
file = open("article.txt", "r")

# Read all contents
content = file.read()

# Count words, lines and characters
words = len(content.split())
lines = len(content.splitlines())
characters = len(content)

# Display the results
print("Number of Words:", words)
print("Number of Lines:", lines)
print("Number of Characters:", characters)

# Close the file
file.close()
