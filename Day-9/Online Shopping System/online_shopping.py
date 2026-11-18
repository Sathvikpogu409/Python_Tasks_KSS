class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ElectronicProduct(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand

class MobilePhone(ElectronicProduct):
    def __init__(self, name, price, brand, model):
        super().__init__(name, price, brand)
        self.model = model

    def display(self):
        print("Product Name:", self.name)
        print("Price:", self.price)
        print("Brand:", self.brand)
        print("Model:", self.model)

m1 = MobilePhone("Smartphone", 25000, "Samsung", "S24")
m1.display()
