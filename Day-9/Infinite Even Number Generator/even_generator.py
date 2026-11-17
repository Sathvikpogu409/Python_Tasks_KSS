# Infinite Even Number Generator (Generators) 
#Create a generator function that continuously generates even numbers starting from 
#2.The program should print the first N even numbers using this generator

def even_numbers():
    num = 2
    while True:
        yield num
        num += 2


n = int(input("Enter how many even numbers: "))

generator = even_numbers()

for i in range(n):
    print(next(generator))
