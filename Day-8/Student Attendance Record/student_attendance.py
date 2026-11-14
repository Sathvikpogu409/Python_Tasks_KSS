#A teacher wants to store student attendance in a file named attendance.txt. Write a
#Python program that takes a student name as input and appends it to the file. Then 
#display the contents of the file.

# Open the file in append mode
file = open("attendance.txt", "a")

# Get student name
name = input("Enter student name: ")

# Append student name to the file
file.write(name + "\n")

# Close the file
file.close()

# Open the file in read mode
file = open("attendance.txt", "r")

# Display file contents
print("\nStudent Attendance:")
print(file.read())

# Close the file
file.close()
