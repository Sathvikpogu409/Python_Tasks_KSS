#University Staff Management (Hierarchical Inheritance) 
#A university has different staff types such as Professor, LabAssistant, and 
#Administrator. All inherit from a base class Staff. Implement hierarchical inheritance 
#to manage and display their information.

class Staff:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Professor(Staff):
    def display(self):
        print("Professor:", self.name)
        print("Salary:", self.salary)


class LabAssistant(Staff):
    def display(self):
        print("Lab Assistant:", self.name)
        print("Salary:", self.salary)


class Administrator(Staff):
    def display(self):
        print("Administrator:", self.name)
        print("Salary:", self.salary)


p = Professor("Ravi", 50000)
l = LabAssistant("Kiran", 30000)
a = Administrator("Priya", 40000)

p.display()
l.display()
a.display()
