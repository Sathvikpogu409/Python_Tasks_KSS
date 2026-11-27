import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Student data
marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]

# 1. Convert into DataFrame
df = pd.DataFrame({
    "Student": students,
    "Marks": marks
})

print(df)

# Pass and Fail calculation
passed = (marks > 50).sum()
failed = (marks <= 50).sum()

# 2. Create Dashboard
plt.figure(figsize=(12, 10))

# Line Graph
plt.subplot(3, 2, 1)
plt.plot(students, marks, marker='o')
plt.title("Student Marks Trend")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid()

# Bar Chart
plt.subplot(3, 2, 2)
plt.bar(students, marks)
plt.title("Student vs Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

# Pie Chart
plt.subplot(3, 2, 3)
plt.pie(
    [passed, failed],
    labels=["Pass", "Fail"],
    autopct="%1.1f%%"
)
plt.title("Pass vs Fail")

# Histogram
plt.subplot(3, 2, 4)
plt.hist(marks, bins=5, edgecolor='black')
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")

# Scatter Plot
plt.subplot(3, 2, 5)
plt.scatter(range(len(marks)), marks)
plt.title("Index vs Marks")
plt.xlabel("Index")
plt.ylabel("Marks")

plt.tight_layout()
plt.show()
