from bank_app.account import account

from bank_app.InsufficientFundsException import InsufficientFundsException
from bank_app.InvalidAmountException import InvalidAmountException
from bank_app.InvalidPinException import InvalidPinException


class bank:
    account_number = 1_000
    registered_account_numbering = 1

    def __init__(self, name):
        self.name = name
        self.accounts = []

    def register_customer(self, first_name: str, last_name: str, pin: str):
        fresh_account = account(first_name, last_name, pin)
        for accountItem in self.accounts:
            if (accountItem.getFirstName().lower() == first_name.lower() and accountItem.getLastName().lower()
                    == last_name.lower()):
                raise ValueError(f"Account {accountItem} already exists")
            if len(pin) > 4 or len(pin) < 4:
                raise InvalidPinException("Invalid Pin")
        fresh_account.account_number = self.account_number
        self.accounts.append(fresh_account)
        self.account_number += self.registered_account_numbering

    def remove_account(self, account_number, pin):
        for accountItem in self.accounts:
            if accountItem.account_number == account_number:
                self.accounts.remove(accountItem)
                return True
        return False

    def get_account_number(self, first_name, last_name):
        for accountItem in self.accounts:
            if (accountItem.getFirstName().lower() == first_name.lower() and accountItem.getLastName().lower()
                    == last_name.lower()):
                return accountItem.account_number
        return None

    def deposit(self, account_number, amount):
        for customer in self.accounts:
            if customer.account_number == account_number:
                if amount <= 0:
                    raise InvalidAmountException("you cannot deposit negative amount")
                customer.balance += amount
        if customer not in self.accounts:
            raise ValueError("Account {} not found".format(account_number))

    def check_balance(self, account_number: str, pin: str):
        for customer in self.accounts:
            if customer.account_number == account_number and customer.isValidPin(pin):
                return customer.balance
        return "Account {} not found".format(account_number)

    def withdraw(self, account_number: int, amount: int, pin: str):
        for customer in self.accounts:
            if customer.account_number == account_number and customer.isValidPin(pin):
                if amount <= 0:
                    raise InvalidAmountException("you cannot withdraw negative amount")
                if customer.balance < amount:
                    raise InsufficientFundsException("insufficient funds")
                customer.balance -= amount
        if customer not in self.accounts:
            return "Account not found"

    def transfer(self, source_account_number: int, destination_account_number: int, amount: int, pin: str):
        for customer in self.accounts:
            if customer.account_number == source_account_number and customer.isValidPin(pin):
                if amount <= 0:
                    raise InvalidAmountException("you cannot transfer negative amount")
                if customer.balance < amount:
                    raise InsufficientFundsException("You have insufficient funds")
                customer.balance -= amount
            if customer.account_number == destination_account_number:
                customer.balance += amount
        if customer.account_number != destination_account_number:
            raise ValueError("Account not found")
        if customer not in self.accounts:
            raise ValueError("Account not found")

    def __str__(self):
        return (f"Account Number: {self.account_number}, Account Balance: #{self.balance}...Thank you for banking with "
                f"us.")

    def find_account(self, account_number: int):
        for customer in self.accounts:
            if customer.account_number == account_number:
                return customer
