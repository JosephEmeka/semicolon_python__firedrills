class account:
    def __init__(self, number: int):
        self.number = number
        self.balance = 0

    def deposit(self, amount: int):
        if amount <= 0:
            raise ValueError("Invalid amount")
        else:
            self.balance += amount

    def getBalance(self):
        return self.balance

    def withdraw(self, amount: int):
        if amount <= 0:
            raise ValueError("Invalid amount")
        else:
            self.balance -= amount

    def isValidNumber(self, number: int):
        if self.number == int(number):
            return True
        else:
            raise ValueError("Invalid number")

    def getNumber(self):
        return self.number
