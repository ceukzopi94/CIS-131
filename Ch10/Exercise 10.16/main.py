"""
Christian Urbanski
CIS 131
09/06/2022

prompts input for user age 
calculates and displays user's maximum heart rate and range of the user's target heart rate
"""
from decimal import Decimal
from tabnanny import check
from savingsaccount import SavingsAccount
from checkingaccount import CheckingAccount

#put constants here

def main(): 
    #put code here
    savings_account = SavingsAccount('Bob Smith', 52084, Decimal(0.25))
    checking_account = CheckingAccount(savings_account.name, 15000, Decimal(3.25))

    interest = savings_account.calculate_interest()
    print(savings_account.balance)
    print(interest)

    print(checking_account.balance)

    checking_account.deposit(interest)

    print(checking_account.balance)




#---------------------------------------------------------------------------------


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
            print ("\n" + prompt + " ", end="")

"""
loop that creates a grid of rows and columns for things to be placed in. 
    for row in range(1, MAX_ROWS + 1):
        for col in range(1, MAX_COLS + 1):
"""

#------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
