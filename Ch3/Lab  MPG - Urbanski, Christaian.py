"""
Christian Urbanski
CIS 131
09/06/2022

prompts input for gallons used while driving, miles driven
calculates and displays user's mpg for that trip
once user enters sentinal value, it will display total MPG
"""

SENTINEL_VALUE = -1 #sentinal value to exit while loop

def main(): 
    #variables to hold totals
    total_gallons = 0
    total_miles = 0

    #ask user for gallons used
    gallons_used = get_valid_float(f'\nEnter many gallons have you used (Enter {SENTINEL_VALUE} to quit): ')

    #checks to see if user entered sentinal value
    while(gallons_used != SENTINEL_VALUE):

        miles_driven = get_valid_float(f'Enter how many miles you drove: ')         #ask user for number of miles driven

        #adds userinput to totals
        total_miles += miles_driven
        total_gallons += gallons_used

        #calculation for miles per gallon
        mpg = miles_driven / gallons_used

        #displays results
        print(f'Miles Per Gallon: {mpg:.1f}')

        #ask user for gallons used
        gallons_used = get_valid_float(f'\nEnter many gallons have you used (Enter {SENTINEL_VALUE} to quit): ')

    #prints overall MPG after exit of while loop
    print(f'\nTotal Miles Driven: {total_miles}')
    print(f'Total Gallons Used: {total_gallons}')
    print(f'Overall MPG: {(total_miles / total_gallons):.1f}\n')

def get_valid_float(msg):
    num = get_float(msg)

    if is_invalid_float(num):
        num = get_float(msg)

    return num

def is_invalid_float(num):
    if num == SENTINEL_VALUE:
        return False

    if(num < 0):
        print('Invalid Amount. Please enter number greater than or equal to 0')
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

#------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
