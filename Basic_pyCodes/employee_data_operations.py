employees = [
    {"name": "John", "age": 25, "salary": 30000},
    {"name": "Alice", "age": 30, "salary": 50000},
    {"name": "Bob", "age": 28, "salary": 40000},
    {"name": "David", "age": 35, "salary": 60000}
]


highest = max(employees, key=lambda x: x["salary"])
print("Highest salary employee:", highest)


filtered = [emp for emp in employees if emp["salary"] > 35000]
print("\nEmployees with salary greater than 35000:")
for emp in filtered:
    print(emp)


total = sum(emp["salary"] for emp in employees)
average = total / len(employees)
print("\nAverage salary:", average)


names = [emp["name"] for emp in employees]
print("\nEmployee names:", names)
