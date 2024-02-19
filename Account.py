from decimal import Decimal


class Account:
    def __init__(self, name: str, balance: Decimal):
        self.__name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount <= Decimal(0.00):
            raise ValueError("amount cannot be less than 0")
        self.balance += amount


a1 = Account("John", Decimal(5000))
print(a1.name)
print(a1.balance)
a1.balance = 10_000
