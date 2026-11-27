import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# SCENARIO 1: DATA LOADING AND CLEANING

df = pd.read_csv("railway_gauges.csv")

print(df.head())
print(df.columns)
print(df.isnull().sum())

df = df.fillna(0)

cols = ['Broad Gauge', 'Metre Gauge',
        'Narrow Gauge', 'Total']

df[cols] = df[cols].apply(
    pd.to_numeric, errors='coerce'
).fillna(0)

# Create graphs folder
os.makedirs("graphs", exist_ok=True)


# SCENARIO 2: LINE GRAPH

plt.figure(figsize=(10, 5))

plt.plot(df['Year'], df['Total'], marker='o')

plt.title("Total Railway Track Growth")
plt.xlabel("Year")
plt.ylabel("Total Tracks")

plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()

plt.savefig("graphs/total_growth.png")
plt.show()


# SCENARIO 3: FILTERING AND BAR CHART

recent = df[
    df['Year'].str[:4].astype(int) > 2000
]

recent = recent[
    ['Year', 'Broad Gauge',
     'Metre Gauge', 'Narrow Gauge']
]

recent.plot(
    x='Year',
    kind='bar',
    figsize=(12, 6)
)

plt.title("Gauge Comparison After 2000")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()
plt.savefig("graphs/gauge_comparison.png")
plt.show()


# SCENARIO 4: PIE CHART

gauge_totals = df[
    ['Broad Gauge', 'Metre Gauge',
     'Narrow Gauge']
].sum()

print(gauge_totals)

plt.figure(figsize=(7, 7))

plt.pie(
    gauge_totals,
    labels=gauge_totals.index,
    autopct='%1.1f%%'
)

plt.title("Gauge Contribution")

plt.savefig("graphs/gauge_contribution.png")
plt.show()


# SCENARIO 5: ADVANCED ANALYSIS

df['% Broad Gauge'] = (
    df['Broad Gauge'] / df['Total']
) * 100

df['% Metre Gauge'] = (
    df['Metre Gauge'] / df['Total']
) * 100

df['% Narrow Gauge'] = (
    df['Narrow Gauge'] / df['Total']
) * 100


# Yearly growth using NumPy

df['Yearly Growth'] = np.diff(
    df['Total'],
    prepend=df['Total'].iloc[0]
)

print("Yearly Growth:")
print(df[['Year', 'Yearly Growth']])


# Line graph for all gauges

plt.figure(figsize=(10, 5))

plt.plot(df['Year'], df['Broad Gauge'],
         label='Broad Gauge')

plt.plot(df['Year'], df['Metre Gauge'],
         label='Metre Gauge')

plt.plot(df['Year'], df['Narrow Gauge'],
         label='Narrow Gauge')

plt.title("Railway Gauge Trends")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.xticks(rotation=45)
plt.legend()
plt.grid()

plt.tight_layout()
plt.savefig("graphs/all_gauges_line.png")
plt.show()


# Stacked bar chart

plt.figure(figsize=(12, 6))

plt.bar(df['Year'], df['Broad Gauge'],
        label='Broad Gauge')

plt.bar(df['Year'], df['Metre Gauge'],
        bottom=df['Broad Gauge'],
        label='Metre Gauge')

bottom = df['Broad Gauge'] + df['Metre Gauge']

plt.bar(df['Year'], df['Narrow Gauge'],
        bottom=bottom,
        label='Narrow Gauge')

plt.title("Railway Gauge Composition")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.xticks(rotation=90)
plt.legend()

plt.tight_layout()
plt.savefig("graphs/stacked_bar.png")
plt.show()


# Highest and lowest growth

print("Highest Growth:")
print(df.loc[df['Yearly Growth'].idxmax()])

print("Lowest Growth:")
print(df.loc[df['Yearly Growth'].idxmin()])

print("Final Analysis Completed!")
