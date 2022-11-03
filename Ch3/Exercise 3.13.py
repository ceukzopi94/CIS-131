"""
Christian Urbanski
CIS 131
09/06/2022

prompts input for user age 
calculates and displays user's maximum heart rate and range of the user's target heart rate
"""

#put constants here

def main(): 
    #put code here
    num_to_factor = get_valid_integer('Enter a number to be facotred: ')
    total = num_to_factor

    for num in range(num_to_factor, 1, -1):

        total *= (num - 1)

    print(f'After faactoring number, total = {total}')

def factor_num(num):
    total = num

    for num in range(num, 1, -1):

        total *= (num - 1)

    return total


def get_valid_integer(msg):
    num = get_integer(msg)

    while is_invalid_num(num):

        num = get_integer(msg)

    return num

def is_invalid_num(num):
    if num < 0:
        print('Please enter a integer 0 or greater...')
        return True

    return False

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
