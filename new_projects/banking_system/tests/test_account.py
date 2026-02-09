# This file contains unit tests for the Account class in the banking system project. 
# Unittest is used to create test cases for the deposit and withdraw methods, 
# is a good practice to ensure that the Account class behaves as expected under various conditions,
# including handling insufficient funds and invalid deposit amounts.
# python -m unittest discover -s tests

import unittest
from accounts import Account, InsufficientFundsError


class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account = Account("123456", "Test User", 100)

    def test_deposit(self):
        self.assertEqual(self.account.deposit(50), 150)

    def test_withdraw(self):
        self.assertEqual(self.account.withdraw(30), 70)

    def test_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsError):
            self.account.withdraw(200)

    def test_negative_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10)


if __name__ == "__main__":
    unittest.main()
