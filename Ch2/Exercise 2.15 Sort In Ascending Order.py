"""
prompts input of 3 floating point numbers to be sorted in asceding order
"""

#put constants here


from cgitb import small


def main(): 
    #put code here
    num1 = get_float("Enter a floating point number: ")
    num2 = get_float("Enter a floating point number: ")
    num3 = get_float("Enter a floating point number: ")

    smallest = num1
    mid = num1
    largest = num1

    if(num2 < smallest):
        smallest = num2
    
    if(num3 < smallest):
        smallest = num3

    if(num2 > largest):
        largest = num2

    if(num3 > largest):
        largest = num3

    if (num1 > smallest and num1 < largest):
        mid = num1

    if(num2 > smallest and num2 < largest):
        mid = num2
    
    if(num3 > smallest and num3 < largest):
        mid = num3

    print(smallest, mid, largest)

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
