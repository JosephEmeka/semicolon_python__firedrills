import unittest

from bank_app.InvalidAmountException import InvalidAmountException
from bank_app.bank import bank


class MyTestCase(unittest.TestCase):

    def test_bank_can_be_created(self):
        gt_bank = bank("GTB")
        self.assertIsInstance(gt_bank, bank)

    def test_bank_has_no_accounts(self):
        self.access_bank = bank("GTB")
        self.assertEqual(0, len(self.access_bank.accounts))

    def test_Customer_can_be_registered(self):
        self.access_bank = bank("GTB")
        self.access_bank.register_customer("Joshua", "mike", "1001")
        self.access_bank.register_customer("Samuel", "Sharon", "1001")
        self.access_bank.register_customer("Ade", "John", "1001")
        self.access_bank.register_customer("David", "Toni", "1001")
        self.assertEqual(4, len(self.access_bank.accounts))

    def test_account_can_be_removed_from_bank(self):
        self.access_bank = bank("GTB")
        self.access_bank.register_customer("Joshua", "mike", "1001")
        self.access_bank.register_customer("Samuel", "Sharon", "1001")
        self.access_bank.register_customer("Ade", "John", "1001")
        account_number = self.access_bank.get_account_number("joshua", "mike")
        self.access_bank.remove_account(account_number)
        self.assertEqual(2, len(self.access_bank.accounts))

    def test_same_bank_account_cannot_be_created_twice(self):
        self.access_bank = bank("GTB")
        self.access_bank.register_customer("joshua", "mike", "1001")
        self.access_bank.register_customer("Samuel", "Sharon", "1001")
        self.access_bank.register_customer("Ade", "John", "1001")
        self.assertEqual(3, len(self.access_bank.accounts))

    def test_that_account_balance_can_be_checked(self):
        self.access_bank = bank("GTB")
        self.access_bank.register_customer("joshua", "mike", "1001")
        self.assertEqual(1, len(self.access_bank.accounts))
        account_number = self.access_bank.get_account_number("joshua", "mike")
        self.assertEqual(0, self.access_bank.check_balance(account_number, "1001"))

    def test_bank_can_deposit_positive_amount_in_accounts(self):
        self.access_bank = bank("GTB")
        self.access_bank.register_customer("Joshua", "mike", "1001")
        self.access_bank.register_customer("Samuel", "Sharon", "1001")
        self.access_bank.deposit(1000, 5000)
        self.assertEqual(5_000, self.access_bank.check_balance(1000, "1001"))

    def test_bank_can_deposit_positive_amount_in_two_different_accounts(self):
        self.access_bank = bank("GTB")
        self.access_bank.register_customer("Joshua", "mike", "1001")
        self.access_bank.register_customer("Samuel", "Sharon", "1003")
        self.access_bank.deposit(1000, 3000)
        self.access_bank.deposit(1001, 7000)
        self.assertEqual(3_000, self.access_bank.check_balance(1000, "1001"))
        self.assertEqual(7_000, self.access_bank.check_balance(1001, "1003"))

    def test_that_bank_account_cannot_receive_negative_deposit(self):
        self.access_bank = bank("Access")
        self.access_bank.register_customer("Joshua", "mike", "1001")
        self.access_bank.register_customer("Samuel", "Sharon", "1001")
        with self.assertRaises(InvalidAmountException):
            self.access_bank.deposit(1000, -3000)
        self.assertEqual(0, self.access_bank.check_balance(1000, "1001"))

    def test_that_bank_account_cannot_receive_deposit_of_amount_zero(self):
        self.access_bank = bank("Access")
        self.access_bank.register_customer("Joshua", "mike", "1001")
        self.access_bank.register_customer("Samuel", "Sharon", "1001")
        with self.assertRaises(InvalidAmountException):
            self.access_bank.deposit(1000, 0)
        self.assertEqual(0, self.access_bank.check_balance(1000, "1001"))

    def test_that_bank_can_withdraw(self):
        self.access_bank = bank("Access")
        self.access_bank.register_customer("Joshua", "mike", "1001")
        self.access_bank.register_customer("Samuel", "Sharon", "1005")
        self.access_bank.deposit(1000, 20_000)
        self.access_bank.deposit(1001, 70_000)
        self.access_bank.withdraw(1000, 5000, "1001")
