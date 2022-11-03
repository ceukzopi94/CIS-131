"""Account class definition"""
from decimal import Decimal

class Account:
    """Account class for maintaining a bank account balance"""
    def __init__(self, name, balance):
        """Initialize an Account object"""

        #if balance is less than 0.00, raise an exception
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be <= 0.00.')
        
        self._name = name
        self._balance = balance

    #funtion to deposit in to the account
    def deposit(self, amount):
        """Deposit money to the account."""

        #if the amount is less than 0.00, raise and exception
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive')
        
        self._balance += amount


    @property #read-only function to get the balance of the account
    def balance(self):
        """Return the balance."""
        return self._balance


    @property # read-only function to get the name of the account
    def name(self):
        """Return the name."""
        return self._name


    # @balance.setter
    # def balance(self, balance):
    #     """Set the balance"""
    #     self._balance = balance