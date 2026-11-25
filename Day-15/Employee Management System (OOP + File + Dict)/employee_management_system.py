class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


employees = {}

for i in range(2):
    name = input("Enter employee name: ")

    try:
        salary = float(input("Enter employee salary: "))

        if salary < 0:
            raise ValueError("Salary cannot be negative")

        emp = Employee(name, salary)
        employees[name] = emp

    except ValueError as e:
        print("Invalid salary:", e)


with open("employees.txt", "w") as file:
    for name, emp in employees.items():
        file.write(f"{emp.name} - {emp.salary}\n")


print("Employee Details:")

for name, emp in employees.items():
    print("Name:", emp.name)
    print("Salary:", emp.salary)
