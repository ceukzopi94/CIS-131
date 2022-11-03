"""
Christian Urbanski
CIS 131
10/10/2022

Program demonstates Fraction class capabilities
"""

from fractions import Fraction

def main(): 
    #declare variables using fraciton class
    first_fraction = Fraction(5, 7)
    second_fraction = Fraction(3, 7)
    
    #calls function to display fractions math
    perform_fraction_math(first_fraction, second_fraction) 

    print('') #adds space for formatting

    #calls function to display the fraction
    display_fraction(first_fraction)
    display_fraction(second_fraction)

    print('')  # adds space for formatting

    #calls function to displat fractions as floats
    display_fraction_as_float(first_fraction)
    display_fraction_as_float(second_fraction)

    print('')  # adds space for formatting

    #creates complex variables by using python built in modules
    first_complex = complex(3, 5) 
    second_complex = complex(4, 6)

    #displays complex numbers
    print(f'First Complex Number: {first_complex}')
    print(f'Second Complex Number: {second_complex}')
    
    #performs and displays math functions on complex numbers
    perform_complex_math(first_complex, second_complex)

    #calls function to display parts of complex numbers
    display_complex_parts(first_complex)
    display_complex_parts(second_complex)

def perform_fraction_math(first_fraction, second_fraction):
    """Function to demonstate Fraction class mathmatic capabilites."""
    print(f'Adding Fractions: {first_fraction} + {second_fraction} = {first_fraction + second_fraction}')
    print(f'Subtracting Fractions: {first_fraction} - {second_fraction} = {first_fraction - second_fraction}')
    print(f'Multipling Fractions: {first_fraction} * {second_fraction} = {first_fraction * second_fraction}')
    print(f'Dividing Fractions: {first_fraction} / {second_fraction} = {first_fraction / second_fraction}')

def display_fraction(fraction):
    """Function to display the fraction numerator and denominator"""
    # this can be accomplished by print(fraction) 
    # but i did it this way to demonstrate that you can grab values individually
    print(f'Fraction: {fraction.numerator}/{fraction.denominator}')

def display_fraction_as_float(fraction):
    """Function to display the fraction as a floating point number."""
    print(f'{fraction} as float: {float(fraction)}')

def perform_complex_math(first_complex, second_complex):
    """Function to display the complex math."""
    print(f'\nAdding Complex Numbers: {first_complex} + {second_complex} = {first_complex + second_complex}')
    print(f'Subtracting Complex Numbers: {first_complex} - {second_complex} = {first_complex - second_complex}')

def display_complex_parts(complex_number):
    """Display the real and imaginary numbers."""
    print(f'\nComplex Number: {complex_number}')
    print(f'Real Number: {complex_number.real}')
    print(f'Imaginary Number: {complex_number.imag}')

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
