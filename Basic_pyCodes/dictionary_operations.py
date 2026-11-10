students = {
    "Sathvik": 85,
    "Rahul": 90,
    "Arjun": 75
}


students["Priya"] = 95


students["Rahul"] = 98


print("Student Details:")

for name, marks in students.items():
    print(name, ":", marks)
