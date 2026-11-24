import numpy as np
import pandas as pd

arr = np.array([
    [100, 200],
    [150, 250],
    [80, 120],
    [300, 400]
])

df = pd.DataFrame(arr, columns=["Sales", "Profit"])

result = df[df["Sales"] > 100]

print("Filtered Data:")
print(result)

print("Average Profit:", result["Profit"].mean())
