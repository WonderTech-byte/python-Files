import unittest

from account.account import Account


class AccountTest(unittest.TestCase):

    def setUp(self):
       self.account = Account(1234)

    def test_pin_is_valid_correct_pin(self):
        self.assertTrue(self.account.pin_is_valid(1234))


    def test_pin_is_valid_incorrect_pin(self):
        self.assertFalse(self.account.pin_is_valid(9999))

    def test_check_balance_correct_pin(self):
        self.assertEqual(self.account.check_balance(1234), 0)

        self.account.deposit_fund(500)
        self.assertEqual(self.account.check_balance(1234), 500)


    def test_check_balance_incorrect_pin(self):
        self.assertEqual(self.account.check_balance(1234), 0)

        self.account.deposit_fund(500)
        self.assertEqual(self.account.check_balance(1234), 500)
        balance = self.account.check_balance(9999)
        self.assertEqual(balance, 0)


    def test_deposit_positive_amount(self):
        self.assertEqual(self.account.check_balance(1234), 0)

        self.account.deposit_fund(200)
        self.assertEqual(self.account.check_balance(1234), 200)

    def test_deposit_zero_or_negative_amount(self):
        self.assertEqual(self.account.check_balance(1234), 0)

        self.account.deposit_fund(500)
        self.assertEqual(self.account.check_balance(1234), 500)

        self.account.deposit_fund(-50)
        self.assertEqual(self.account.check_balance(1234), 500)


    def test_withdraw_correct_pin_with_sufficient_balance(self):
        self.assertEqual(self.account.check_balance(1234), 0)

        self.account.deposit_fund(500)
        self.assertEqual(self.account.check_balance(1234), 500)

        self.account.withdraw_fund(200, 1234)
        self.assertEqual(self.account.check_balance(1234), 300)

    def test_withdraw_incorrect_pin(self):
        self.assertEqual(self.account.check_balance(1234), 0)

        self.account.deposit_fund(500)
        self.assertEqual(self.account.check_balance(1234), 500)

        self.account.withdraw_fund(200, 9999)
        self.assertEqual(self.account.check_balance(1234), 500)

    def test_withdraw_insufficient_balance(self):
        self.assertEqual(self.account.check_balance(1234), 0)

        self.account.deposit_fund(100)

        self.account.withdraw_fund(200, 1234)
        self.assertEqual(self.account.check_balance(1234), 100)

    def test_withdraw_zero_or_negative_amount(self):
        self.assertEqual(self.account.check_balance(1234), 0)

        self.account.deposit_fund(300)
        self.assertEqual(self.account.check_balance(1234), 300)
        self.account.withdraw_fund(0, 1234)
        self.assertEqual(self.account.check_balance(1234), 300)

        self.account.withdraw_fund(-50, 1234)
        self.assertEqual(self.account.check_balance(1234), 300)

