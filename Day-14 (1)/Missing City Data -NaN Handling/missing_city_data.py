import pandas as pd

cities = {
    "Delhi": 2000000,
    "Mumbai": 3000000,
    "Chennai": 1500000
}

my_cities = ["Delhi", "Chennai", "Bangalore"]

S = pd.Series(cities, index=my_cities)

print(S)

print("Missing Values:")
print(S.isnull())
