#put constants here


def main(): 
    #put code here
    
    num1 = get_integer("Please enter the first number ")
    num2 = get_integer("Please enter the second number ")
    num3 = get_integer("Please enter the third number ")

    total = num1 + num2 + num3
    avg = total / 3
    pro = num1 * num2 * num3

    smallest = num1

    if(num2 < smallest):
        smallest = num2
    if(num3 < smallest):
        smallest = num3

    largest = num1
    
    if(num2 > largest):
        largest = num2
    if(num3 > largest):
        largest = num3

    print('total', total)
    print('average', avg)
    print('product',pro)
    print('smallest', smallest)
    print('largest', largest)
    
#---------------------------------------------------------------------------------

def calc_sum(num1, num2):
    sum = num1 + num2
    return sum

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
