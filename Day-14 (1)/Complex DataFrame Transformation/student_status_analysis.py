import pandas as pd

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D"],
    "Marks": [50, 80, 30, 90]
})

df["Status"] = df["Marks"].apply(
    lambda x: "Fail" if x < 50 else "Pass"
)

print("Student Data:")
print(df)

passed = df[df["Status"] == "Pass"]

print("Passed Students:")
print(passed)

average = passed["Marks"].mean()

print("Average Marks of Passed Students:", average)
