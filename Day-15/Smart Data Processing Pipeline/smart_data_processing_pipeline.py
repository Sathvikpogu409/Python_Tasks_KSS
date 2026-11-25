import numpy as np
import pandas as pd
import time


def calculate_time(func):

    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print("Execution Time:", end - start, "seconds")

        return result

    return wrapper


def read_numbers(filename):
    with open(filename, "r") as file:
        for line in file:
            try:
                yield float(line.strip())

            except ValueError:
                print("Invalid data:", line.strip())


@calculate_time
def process_data():

    numbers = list(read_numbers("numbers.txt"))

    if not numbers:
        print("No valid numbers found")
        return

    arr = np.array(numbers)

    mean = np.mean(arr)
    std = np.std(arr)

    df = pd.DataFrame({
        "Mean": [mean],
        "Standard Deviation": [std]
    })

    print(df)


try:
    process_data()

except FileNotFoundError:
    print("File not found")

except Exception as e:
    print("Error:", e)
