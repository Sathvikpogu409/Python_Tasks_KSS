students = {
    "Rahul": 85,
    "Priya": 90,
    "Arjun": 78
}

highest_student = max(students, key=students.get)

print("Student with highest marks:", highest_student)
print("Highest marks:", students[highest_student])
