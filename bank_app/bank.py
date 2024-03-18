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
                raise ValueError(f"Account {accountItem.account_number} already exists")
            if len(pin) != 4:
                raise InvalidPinException("Invalid Pin")
        fresh_account.account_number = self.account_number
        self.accounts.append(fresh_account)
        self.account_number += self.registered_account_numbering

    def remove_account(self, account_number, pin):
        for accountItem in self.accounts:
            if accountItem.account_number == account_number and accountItem.isValidPin(pin):
                self.accounts.remove(accountItem)
                return True
        raise ValueError("Account {} not found".format(account_number))

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
                    raise InvalidAmountException("You cannot deposit a negative amount")
                customer.balance += amount
                return
        raise ValueError("Account {} not found".format(account_number))

    def check_balance(self, account_number: str, pin: str):
        for customer in self.accounts:
            if customer.account_number == account_number and customer.isValidPin(pin):
                return customer.balance
        raise ValueError("Account {} not found".format(account_number))

    def withdraw(self, account_number: int, amount: int, pin: str):
        for customer in self.accounts:
            if customer.account_number == account_number and customer.isValidPin(pin):
                if amount <= 0:
                    raise InvalidAmountException("You cannot withdraw a negative amount")
                if customer.balance < amount:
                    raise InsufficientFundsException("Insufficient funds")
                customer.balance -= amount
                return
        raise ValueError("Account {} not found".format(account_number))

    def transfer(self, source_account_number: int, destination_account_number: int, amount: int, pin: str):
        source_customer = None
        destination_customer = None
        for customer in self.accounts:
            if customer.account_number == source_account_number and customer.isValidPin(pin):
                if amount <= 0:
                    raise InvalidAmountException("You cannot transfer a negative amount")
                if customer.balance < amount:
                    raise InsufficientFundsException("You have insufficient funds for the transfer")
                source_customer = customer
            if customer.account_number == destination_account_number:
                destination_customer = customer

        if source_customer is None:
            raise ValueError("Source Account not found")

        if destination_customer is None:
            raise ValueError("Destination Account not found")

        source_customer.balance -= amount
        destination_customer.balance += amount

    def __str__(self):
        return f"Bank: {self.name}, Number of Accounts: {len(self.accounts)}"

    def find_account(self, account_number: int):
        for customer in self.accounts:
            if customer.account_number == account_number:
                return customer
        raise ValueError("Account {} not found".format(account_number))
