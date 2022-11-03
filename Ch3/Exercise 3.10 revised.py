"""
Christian Urbanski
CIS 131 
09/01/2022

This script calclates the interest gained onstarting balance
and displays the total account balance after a set number of years
"""

#put constants here
INTEREST_RATE = 0.07
YEAR_DIFF = 10

def main(): 
    #put code here
    principle = 1000.00
    num_of_years = 30

    print(f'Starting Balance: {principle}')

    for year in range(1, num_of_years):
        bal = calc_interest_rate(principle, year)
        print(f'After {year} years, {bal:.2f}')

#---------------------------------------------------------------------------------

def calc_interest_rate(p, years):
    #interest equation a = p(1 + r)^n
    a = p * ((1 + INTEREST_RATE) ** years)
    return a

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
