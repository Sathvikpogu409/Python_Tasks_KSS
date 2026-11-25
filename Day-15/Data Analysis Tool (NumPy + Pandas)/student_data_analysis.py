import numpy as np
import pandas as pd

marks = np.random.randint(30, 101, 5)

df = pd.DataFrame({
    "Student": ["A", "B", "C", "D", "E"],
    "Marks": marks
})

print("Student Data:")
print(df)

passed = df[df["Marks"] >= 40]

print("Passing Students:")

for index, row in passed.iterrows():
    print(row["Student"], row["Marks"])

average = np.mean(marks)

print("Average Marks:", average)
