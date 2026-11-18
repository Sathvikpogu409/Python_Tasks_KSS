class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display(self):
        print("Account Number:", self.account_number)
        print("Current Balance:", self.balance)

b1 = BankAccount(12345, 10000)

b1.deposit(2000)
b1.withdraw(3000)
b1.display()
