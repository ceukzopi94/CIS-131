"""
Christian Urbanski
CIS 131
10/5/2022

imports classes from py files and displayes thetime and time in seconds since midnight.
"""

from timewithpropertires import Time
from timeinseconds import Time as TimeInSeconds

#put constants here

def main(): 
    #put code here
    current_time = Time() #makes an object from timewithproperties
    current_seconds = TimeInSeconds() # makes object from timeinseconds

    print(current_time)
    print(current_seconds)

    current_time.time = (14, 45, 53) #sets time to a tuple of time in (hour, minute, second) format
    current_seconds.set_time(current_time.time) #passes tuple to set time in seconds
    
    print(current_time)
    print(current_seconds)
    

    



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
