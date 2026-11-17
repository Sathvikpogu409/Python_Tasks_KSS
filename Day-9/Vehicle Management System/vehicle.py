#Vehicle Management System (Inheritance) 
#A transport company manages different vehicles. Create a base class Vehicle with 
#attributes like brand and speed. Create derived classes Car and Bike that inherit from 
#Vehicle and display their details.

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed


class Car(Vehicle):
    def display(self):
        print("Car Brand:", self.brand)
        print("Speed:", self.speed)


class Bike(Vehicle):
    def display(self):
        print("Bike Brand:", self.brand)
        print("Speed:", self.speed)


c1 = Car("Toyota", 120)
b1 = Bike("Honda", 80)

c1.display()
b1.display()
