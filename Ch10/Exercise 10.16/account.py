"""Account class definition"""
from decimal import Decimal

from pandas import value_counts

class Account:
    """Account class for maintaining a bank account balance"""
    def __init__(self, name, balance):
        """Initialize an Account object"""
        
        self.name = name
        self.balance = balance


    @property #read-only function to get the balance of the account
    def balance(self):
        """Return the balance."""
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Set the balance"""

        #if balance is less than 0.00, raise an exception
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be <= 0.00.')

        self._balance = Decimal(balance)


    @property # read-only function to get the name of the account
    def name(self):
        """Return the name."""
        return self._name

    @name.setter
    def name(self, new_name):
        """Set the name."""
        self._name = new_name


    #funtion to deposit in to the account
    def deposit(self, amount):
        """Deposit money to the account."""

        #if the amount is less than 0.00, raise and exception
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive')

        self.balance += Decimal(amount)

    #funtion to withdraw in to the account
    def withdraw(self, amount):
        """Deposit money to the account."""

        #if the amount is less than 0.00, raise and exception
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive')
        
        if amount > self.balance:
            raise ValueError('Not enough funds for transaction.')

        self.balance -= Decimal(amount)
