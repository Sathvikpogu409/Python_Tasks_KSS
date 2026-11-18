class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def display(self):
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)

m1 = Manager("Rahul", 50000)
m1.display()
