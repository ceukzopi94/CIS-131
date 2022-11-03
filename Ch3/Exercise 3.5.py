"""
Christian Urbanski
CIS 131
09/06/2022

prompts input for user age 
calculates and displays user's maximum heart rate and range of the user's target heart rate
"""

#put constants here

from tkinter import getint


def main(): 
    #put code here
    print('Enter two integers, and i will tell you\
        the relationships the satisfy')

    num1 = get_integer('Enter first int: ')
    num2 = get_integer('Enter second int: ')

    if num1 == num2:
        print(f'{num1} is equal to {num2}')
    else:
        print(f'{num1} is not equal to {num2}')

    if num1 < num2:
        print(f'{num1} is less than {num2}')
    else:
        print(f'{num1} is greater than {num2}')

    if num1 <= num2:
        print(f'{num1} is less than or equal to {num2}')
    else:
        print(f'{num1} is greater than to {num2}')


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
