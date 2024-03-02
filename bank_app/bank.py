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
        fresh_account.account_number = self.account_number
        self.accounts.append(fresh_account)
        self.account_number += self.registered_account_numbering

    def remove_account(self, account_number):
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

    # def sort_accounts(self):
    #     self.accounts.sort(key = lambda my_account: my_account.account_number)

    def deposit(self, account_number, amount):
        for customer in self.accounts:
            if customer.account_number == account_number:
                if amount <= 0:
                    raise InvalidAmountException("you cannot deposit negative amount")
                customer.balance += amount

    def check_balance(self, account_number: str, pin: str):
        for customer in self.accounts:
            if customer.account_number == account_number and customer.isValidPin(pin):
                return customer.balance
        return None

    def withdraw(self, account_number: int, amount: int, pin: str):
        for customer in self.accounts:
            if customer.account_number == account_number and customer.isValidPin(pin):
                customer.balance -= amount

        

