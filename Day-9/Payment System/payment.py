#Payment System (Runtime Polymorphism) 
#An online store supports multiple payment methods: CreditCard, UPI, and 
#NetBanking. Create a base class Payment with a method process_payment() and 
#override it in each payment type.

class Payment:
    def process_payment(self):
        print("Processing payment")


class CreditCard(Payment):
    def process_payment(self):
        print("Payment through Credit Card")


class UPI(Payment):
    def process_payment(self):
        print("Payment through UPI")


class NetBanking(Payment):
    def process_payment(self):
        print("Payment through Net Banking")


p1 = CreditCard()
p2 = UPI()
p3 = NetBanking()

p1.process_payment()
p2.process_payment()
p3.process_payment()
