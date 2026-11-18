class Staff:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Professor(Staff):
    def display(self):
        print("Professor Name:", self.name)
        print("Salary:", self.salary)

class LabAssistant(Staff):
    def display(self):
        print("Lab Assistant Name:", self.name)
        print("Salary:", self.salary)

class Administrator(Staff):
    def display(self):
        print("Administrator Name:", self.name)
        print("Salary:", self.salary)

p1 = Professor("Rahul", 50000)
l1 = LabAssistant("Priya", 30000)
a1 = Administrator("Arjun", 40000)

p1.display()
print("----------------")
l1.display()
print("----------------")
a1.display()
