from decimal import Decimal

from bank_app.InsufficientFundsException import InsufficientFundsException
from bank_app.InvalidAmountException import InvalidAmountException
from bank_app.InvalidPinException import InvalidPinException


class account:

    def __init__(self, first_name: str, last_name: str, pin: str):
        self.first_name = first_name
        self.last_name = last_name
        self.pin = pin
        self.balance = 0
        self.account_number = None

    def deposit(self, amount: int):
        if amount <= Decimal(0.0):
            raise ValueError("Invalid amount")
        else:
            self.balance += amount

    def check_balance(self):
        return self.balance

    def withdraw(self, amount: int, pin: str):
        self.isValidPin(pin)
        if amount <= 0:
            raise InvalidAmountException("Invalid amount")
        if amount > self.balance:
            raise InsufficientFundsException("Insufficient fund")
        else:
            self.balance -= amount

    def isValidPin(self, pin: str):
        if len(pin) > 4 or len(pin) < 4:
            raise InvalidPinException("Invalid Pin")
        if self.pin == str(pin):
            return True
        else:
            raise ValueError("Invalid pin number")

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name
