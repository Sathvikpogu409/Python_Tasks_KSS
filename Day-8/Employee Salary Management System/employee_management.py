#A company stores employee data in a file employees.txt in the format: EmployeeName Salary

# Open the file in read mode
file = open("employees.txt", "r")

employees = {}

print("Employee Details:")

# Read employee records
for line in file:
    name, salary = line.split()
    employees[name] = int(salary)
    print(name, salary)

file.close()

# Find employee with the highest salary
if employees:
    highest_employee = max(employees, key=employees.get)

    print("\nEmployee with Highest Salary:")
    print(highest_employee, ":", employees[highest_employee])

# Append a new employee record
file = open("employees.txt", "a")

name = input("\nEnter new employee name: ")
salary = int(input("Enter salary: "))

file.write(name + " " + str(salary) + "\n")

file.close()

print("New employee record added successfully.")
