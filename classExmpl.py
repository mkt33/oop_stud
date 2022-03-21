class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

a = BankAccount()
b = BankAccount()
balA = a.deposit(100)
print("A:", balA)
balB = b.deposit(50)
print("B:",balB)
balB = b.withdraw(10)
print("B:",balB)
balA = a.withdraw(10)
print("A:",balA)