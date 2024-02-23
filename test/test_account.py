import unittest

from bank_app import *
from bank_app.account import *


class TestAccount(unittest.TestCase):
    def test_account_creation(self):
        my_account = account(1000000000)
        self.assertTrue(my_account)
        self.assertIsInstance(my_account, account)

    def test_deposit_5k_balance_increases(self):
        my_account = account(1_000_000_000)
        my_account.deposit(5000)
        self.assertEqual(5_000, my_account.getBalance())

    def test_deposit_5k_twice_withdraw2k_balance_remains8k(self):
        my_account = account(1_000_000_000)
        my_account.deposit(5_000)
        my_account.deposit(5_000)
        my_account.withdraw(2_000)
        self.assertEqual(8_000, my_account.getBalance())

    def test_deposit_negative_amount_throws_exception(self):
        my_account = account(1_000_000_000)
        my_account.deposit(5_000)
        my_account.deposit(5_000)
        my_account.withdraw(2_000)
        self.assertEqual(8_000, my_account.getBalance())
        with self.assertRaises(ValueError):
            my_account.deposit(-15000)

    def test_deposit_5K_twice_withdraw_negative_amount(self):
        my_account = account(1_000_000_000)
        my_account.deposit(5_000)
        my_account.deposit(5_000)
        with self.assertRaises(ValueError):
            my_account.withdraw(-2_000)

    def test_deposit_5k_Twice_withdraw_5K_validate_account_number(self):
        my_account = account(1_000_000_000)
        my_account.deposit(5_000)
        my_account.deposit(5_000)
        self.assertEqual(my_account.isValidNumber, my_account.getNumber()) 
        with self.assertRaises(ValueError):
            my_account.withdraw(-2_000)
