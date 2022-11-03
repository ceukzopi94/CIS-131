"""
Christian Urbanski
CIS 131
10/08/2022
Assignment: Manipulating Dates and Times With Module: DATETIME

This program shows the capabilies of pythons built in module datetime
"""
from datetime import datetime
#put constants here

def main(): 
    #grabs the current date and time
    x = datetime.now()
    y = datetime.now()
    
    #calls function to display datetime attributes
    display_datetime_attributes(x)
    display_datetime_attributes(y)

    #function to compair the times
    compaire_times(x, y)

    #prints the difference in time
    print(x - y)


def display_datetime_attributes(datetime_var):
    """Function that displays each attribue of datetime."""
    print(f'Date: {datetime_var}\n' +
        f'Year: {datetime_var.strftime("%Y")}\n' +
        f'Month: {datetime_var.strftime("%m")}\n' +
        f'Day: {datetime_var.strftime("%d")}\n' +
        f'Hour: {datetime_var.strftime("%H")}\n' +
        f'Minute: {datetime_var.strftime("%M")}\n' +
        f'Second: {datetime_var.strftime("%S")}\n' +
        f'Micro-Second: {datetime_var.strftime("%f")}\n')


def compaire_times(first_time, second_time):
    """Function to compair the times and display if they are equal or not."""
    if first_time == second_time:
        print('Times are the same.')
    elif first_time > second_time:
        print('first time is greater than second time.')
    elif first_time < second_time:
        print('Second time is greater than first time.')
    else:
        print('Error: Times were not compaired properly...')

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
