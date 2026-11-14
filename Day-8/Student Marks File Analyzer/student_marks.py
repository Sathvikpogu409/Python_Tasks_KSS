#A teacher stores student marks in a file marks.txt in the format: 
#Name Marks

# Open the file in read mode
file = open("marks.txt", "r")

total = 0
count = 0

print("Student Records:")

# Read each line from the file
for line in file:
    name, marks = line.split()

    marks = int(marks)

    print(name, marks)

    total += marks
    count += 1

# Close the file
file.close()

# Calculate class average
if count > 0:
    average = total / count
    print("Average Marks:", average)
else:
    print("No student records found.")
