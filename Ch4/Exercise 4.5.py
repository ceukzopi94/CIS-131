"""
Christian Urbanski
CIS 131
09/06/2022

hours since midnight
"""

#put constants here

def main(): 
    #put code here
    hour = 11
    minute = 43 
    seconds = 25

    time = (hour, minute, seconds)

    #sec_since_mid = seconds_since_midnight(time)

    print(seconds_since_midnight(time))
    
def seconds_since_midnight(time):
    """Calculates time since midnight"""
    hour, minute, seconds = time

    hour_in_seconds = hour * 60 * 60
    minute_in_seconds = minute * 60

    time = (hour_in_seconds, minute_in_seconds, seconds)
    return hour_in_seconds + minute_in_seconds + seconds

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
