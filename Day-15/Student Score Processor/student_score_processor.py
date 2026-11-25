import math

students = [
    ("Rahul", 75),
    ("Amit", 45),
    ("Priya", 85),
    ("Sneha", 60)
]

student_dict = dict(students)

print("Students scoring above 50:")

passed = []

for name, marks in student_dict.items():
    if marks > 50:
        print(name, marks)
        passed.append(marks)

average = math.fsum(student_dict.values()) / len(student_dict)

print("Average marks:", average)

with open("student_results.txt", "w") as file:
    file.write("Student Results\n")
    for name, marks in student_dict.items():
        file.write(f"{name}: {marks}\n")

    file.write(f"Average Marks: {average}\n")
