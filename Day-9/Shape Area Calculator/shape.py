import math

class Circle:
    def area(self):
        radius = 5
        print("Circle Area:", math.pi * radius * radius)

class Rectangle:
    def area(self):
        length = 10
        width = 5
        print("Rectangle Area:", length * width)

class Triangle:
    def area(self):
        base = 10
        height = 5
        print("Triangle Area:", 0.5 * base * height)

shapes = [Circle(), Rectangle(), Triangle()]

for shape in shapes:
    shape.area()
