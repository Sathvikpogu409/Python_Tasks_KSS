#Shape Area Calculator (Polymorphism) 
#A graphics application needs to calculate the area of different shapes. Create classes 
#Circle, Rectangle, and Triangle, each having an area() method. Demonstrate 
#polymorphism by calling the same method for different objects.


class Circle:
    def area(self):
        r = 5
        return 3.14 * r * r


class Rectangle:
    def area(self):
        length = 10
        width = 5
        return length * width


class Triangle:
    def area(self):
        base = 10
        height = 6
        return 0.5 * base * height


c = Circle()
r = Rectangle()
t = Triangle()

for shape in (c, r, t):
    print("Area:", shape.area())
