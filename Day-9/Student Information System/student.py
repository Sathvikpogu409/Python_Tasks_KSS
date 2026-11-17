#A school wants a program to store student details. Create a Student class with 
#attributes such as name, roll number, and marks. Create objects for at least three 
#students and display their details.


class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)
        print()


s1 = Student("Sathvik", 101, 85)
s2 = Student("Rahul", 102, 90)
s3 = Student("Priya", 103, 95)

s1.display()
s2.display()
s3.display()
