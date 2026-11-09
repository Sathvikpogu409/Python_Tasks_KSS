students = {
    "Rahul": 85,
    "Amit": 92,
    "Priya": 78,
    "Sneha": 95
}


sorted_students = dict(sorted(students.items(), key=lambda x: x[1], reverse=True))

print("Students sorted by marks:")

for name, marks in sorted_students.items():
    print(name, ":", marks)


print("\nTop two students:")

for name, marks in list(sorted_students.items())[:2]:
    print(name, ":", marks)
