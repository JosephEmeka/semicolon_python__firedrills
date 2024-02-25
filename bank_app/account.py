from decimal import Decimal


class account:
    def __init__(self, pin: str):
        self.pin = pin
        self.balance = 0

    @property
    def balance(self):
        return self.balance

    @balance.setter
    def balance(self, value: Decimal):
        if value <= value:
            raise ValueError("")
        return self.balance

    def deposit(self, amount: int):
        if amount <= Decimal(0.0):
            raise ValueError("Invalid amount")
        else:
            self.balance += amount

    def getBalance(self):
        return self.balance

    def withdraw(self, amount: int, pin: str):
        self.isValidPin(pin)
        if amount <= 0:
            raise ValueError("Invalid amount")
        else:
            self.balance -= amount

    def isValidPin(self, pin: str):
        if self.pin == str(pin):
            return True
        else:
            raise ValueError("Invalid number")

