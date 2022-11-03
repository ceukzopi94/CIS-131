"""Savings Account Sub Class"""

#from Ch10.Exercise 10.16.account import Account
from decimal import Decimal
from account import Account

class SavingsAccount(Account):
    """Savings Account Sub Class."""

    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)

        self.interest_rate = interest_rate

    @property
    def interest_rate(self):
        """Return the interest rate."""
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, rate):
        """Sets the interest rate."""
        if not rate >= Decimal('0.00'):
            raise ValueError('Interest rate must be a positive number.')

        self._interest_rate = Decimal(rate)

    def calculate_interest(self):
        """Calculates the interest earned of the savings account."""
        return self.balance * self.interest_rate