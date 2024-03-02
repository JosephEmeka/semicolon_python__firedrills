import unittest
from bank_app.account import *


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.my_account = account("Stanley", "Michael", "1234")

    def test_account_creation(self):
        self.assertIsInstance(self.my_account, account)

    def test_deposit_5k_balance_increases(self):
        self.my_account.deposit(5000)
        self.assertEqual(5_000, self.my_account.check_balance())

    def test_deposit_5k_twice_withdraw2k_balance_remains8k(self):
        self.my_account.deposit(5_000)
        self.my_account.deposit(5_000)
        self.my_account.withdraw(2_000, "1234")
        self.assertEqual(8_000, self.my_account.check_balance())

    def test_deposit_negative_amount_throws_exception(self):
        self.my_account.deposit(5_000)
        self.my_account.deposit(5_000)
        self.my_account.withdraw(2_000, "1234")
        self.assertEqual(8_000, self.my_account.check_balance())
        with self.assertRaises(ValueError):
            self.my_account.deposit(-15000)

    def test_deposit_5K_twice_withdraw_negative_amount(self):
        self.my_account.deposit(5_000)
        self.my_account.deposit(5_000)
        with self.assertRaises(InvalidAmountException):
            self.my_account.withdraw(-2_000, "1234")

    def test_deposit_5K_twice_withdraw_zero(self):
        self.my_account.deposit(5_000)
        self.my_account.deposit(5_000)
        with self.assertRaises(InvalidAmountException):
            self.my_account.withdraw(0, "1234")

    def test_deposit_5k_Twice_withdraw_5K(self):
        self.my_account.deposit(5_000)
        self.my_account.deposit(5_000)
        self.assertEqual(10_000, self.my_account.check_balance())
        self.my_account.withdraw(7_000, "1234")
        self.assertEqual(3_000, self.my_account.check_balance())

    def test_deposit_5k_withdraw_2K_invalid_pin(self):
        self.my_account.deposit(5_000)
        self.my_account.withdraw(2000, "1234")
        self.assertEqual(3_000, self.my_account.check_balance())
        self.assertTrue(self.my_account.isValidPin("1234"))

    def test_deposit_5k_withdraw_15K_validatePin_insufficient_fund(self):
        self.my_account.deposit(5_000)
        self.assertEqual(5_000, self.my_account.check_balance())
        self.assertTrue(self.my_account.isValidPin)
        with self.assertRaises(InsufficientFundsException):
            self.my_account.withdraw(15_000, "1234")


