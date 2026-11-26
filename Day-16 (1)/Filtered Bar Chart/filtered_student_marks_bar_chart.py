import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks = np.array([45, 80, 60, 30, 90])

names = ["A", "B", "C", "D", "E"]

df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

print("Complete Data:")
print(df)

filtered = df[df["Marks"] > 50]

print("Filtered Students:")
print(filtered)

plt.bar(filtered["Name"], filtered["Marks"])

plt.xlabel("Student Names")
plt.ylabel("Marks")

plt.title("Students Scoring Above 50")

plt.show()
