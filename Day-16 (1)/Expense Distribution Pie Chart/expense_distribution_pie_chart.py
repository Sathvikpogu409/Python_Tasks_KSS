import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

expenses = np.array([500, 300, 200])

labels = ["Food", "Rent", "Travel"]

df = pd.DataFrame({
    "Expenses": labels,
    "Amount": expenses
})

print(df)

plt.pie(
    df["Amount"],
    labels=df["Expenses"],
    autopct="%1.1f%%"
)

plt.title("Monthly Expense Distribution")

plt.show()
