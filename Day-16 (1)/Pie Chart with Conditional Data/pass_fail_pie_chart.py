import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

scores = np.array([40, 60, 80, 30, 90])

passed = np.sum(scores > 50)

failed = np.sum(scores <= 50)

df = pd.DataFrame({
    "Result": ["Pass", "Fail"],
    "Count": [passed, failed]
})

print(df)

plt.pie(
    df["Count"],
    labels=df["Result"],
    autopct="%1.1f%%"
)

plt.title("Pass vs Fail Distribution")

plt.show()
