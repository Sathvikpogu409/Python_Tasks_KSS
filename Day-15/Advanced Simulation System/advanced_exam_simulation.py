import random
import numpy as np
import pandas as pd
import math


class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):

        if self.marks >= 90:
            return "A"

        elif self.marks >= 75:
            return "B"

        elif self.marks >= 60:
            return "C"

        elif self.marks >= 40:
            return "D"

        else:
            return "Fail"


try:
    names = ["Rahul", "Amit", "Priya", "Sneha", "Ravi"]

    marks = np.array([
        random.randint(0, 100) for i in range(5)
    ])

    students = []

    for i in range(5):
        student = Student(names[i], marks[i])
        students.append(student)

    grades = []

    for student in students:
        grades.append(student.calculate_grade())

    df = pd.DataFrame({
        "Name": names,
        "Marks": marks,
        "Grade": grades
    })

    print("Exam Results:")
    print(df)

    average = math.fsum(marks) / len(marks)

    print("Average Marks:", average)
    print("Highest Marks:", max(marks))
    print("Lowest Marks:", min(marks))

    df.to_csv("exam_report.csv", index=False)

    print("Report saved successfully")

except Exception as e:
    print("Error:", e)
