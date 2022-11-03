"""Savings Account Sub Class"""

#from Ch10.Exercise 10.16.account import Account
from decimal import Decimal
from account import Account

class CheckingAccount(Account):
    """Checking Account Sub Class."""

    def __init__(self, name, balance, fee):
        super().__init__(name, balance)

        self.transaction_fee = fee

    @property
    def transaction_fee(self):
        """Return the transaction fee."""
        return self._transaction_fee

    @transaction_fee.setter
    def transaction_fee(self, fee):
        """Sets the transaction fee amount."""
        if not fee >= 0:
            raise ValueError('Fee must be greater than or equal to 0.')
        
        self._transaction_fee = Decimal(fee)


    def deposit(self, amount):
        """Deposit into checking account."""
        if not amount >= Decimal('0.00'):
            raise ValueError('Amount must be greater than or equal to 0.')

        super().deposit(amount - self.transaction_fee)


    def withdraw(self, amount):
        """Withdraw from checking account."""
        if not amount >= Decimal('0.00'):
            raise ValueError('Amount must be greater than or equal to 0.')

        super().withdraw(amount + self.transaction_fee)