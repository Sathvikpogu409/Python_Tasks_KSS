#Employee Bonus Calculator (Decorators & OOP) 
#A company wants to apply a bonus calculation automatically before displaying the 
#salary. Create an Employee class and use a decorator that modifies the salary by 
#adding a bonus before displaying it.

def add_bonus(func):
    def wrapper(self):
        bonus = 5000
        updated_salary = self.salary + bonus
        func(self, updated_salary)
    return wrapper


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @add_bonus
    def display_salary(self, salary):
        print("Employee Name:", self.name)
        print("Salary with Bonus:", salary)


e = Employee("Rahul", 30000)
e.display_salary()
