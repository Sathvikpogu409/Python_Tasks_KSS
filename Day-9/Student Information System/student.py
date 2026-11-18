
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)
        print("----------------")

s1 = Student("Rahul", 101, 85)
s2 = Student("Priya", 102, 90)
s3 = Student("Arjun", 103, 78)

s1.display()
s2.display()
s3.display()
