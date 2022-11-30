"""Account class definition"""
from decimal import Decimal

class Credits:
    """Account class for maintaining a bank account balance"""
    def __init__(self, balance):
        """Initialize an Account object"""
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


    #funtion to deposit in to the account
    def deposit(self, amount):
        """Deposit money to the account."""

        #if the amount is less than 0.00, raise and exception
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive')

        self.balance += Decimal(amount)


    #funtion to withdraw in to the account
    def withdraw(self, amount):
        """Widthdraw money from the machine."""

        #if the amount is less than 0.00, raise and exception
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive')
        
        if amount > self.balance:
            raise ValueError('Not enough funds for transaction.')

        self.balance -= Decimal(amount)

        #funtion to withdraw in to the account


    def cash_out(self):
        """Cash out balance from machine."""
        print(f'Cash Out Amount: {self.balance}')

        self.balance = 0


    def get_deposit(self):
        """Function to get a deposit from the player."""
        is_depositing = get_yes_or_no('Would you like to deposit credits into the machine? (y/n) ')

        if (is_depositing):
            self.deposit(get_positive_int('Enter amount to deposit: '))


def get_positive_int(msg):
    """Function to get positive number."""
    number = get_integer(msg)

    while (number < 0):
        print('Please enter positive number.')
        number = get_integer(msg)

    return number


def get_integer(message, prompt="none"):
    while True:
        display_prompt(message, prompt)
        try:
            newValue = int(input())
            return newValue
        except ValueError:
            print('Error: non-numeric value entered')


def get_float(message, prompt="none"):
    while True:
        display_prompt(message, prompt)
        try:
            newValue = float(input())
            return newValue
        except ValueError:
            print('Error: non-numeric value entered')


def get_string(message, prompt="none"):
    while True:
        display_prompt(message, prompt)
        newValue = input()
        if newValue and newValue.strip():
            return newValue
        else:
            print('Error: no data entered')


def get_yes_or_no(message, prompt="none"):
    while True:
        new_value = get_string(message, prompt)
        new_value = new_value.lower()
        if new_value == "y" or new_value == "yes":
            return True
        if new_value == "n" or new_value == "no":
            return False
        print('Error: invalid value entered')


def display_prompt(message, prompt):
    print(message, end="")
    if prompt != "none":
        print("\n" + prompt + " ", end="")
