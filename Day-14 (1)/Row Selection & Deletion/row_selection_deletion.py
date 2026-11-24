import pandas as pd

df = pd.DataFrame({
    "A": [10, 20, 30],
    "B": [5, 15, 25]
}, index=["x", "y", "z"])

print("Selected Row:")
print(df.loc["y"])

df = df.drop("x")

print("Updated DataFrame:")
print(df)
