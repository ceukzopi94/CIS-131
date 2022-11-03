#put constants here


def main(): 
    #put code here
    num_to_input = 4
    smallest = 0
    largest = 0
    total = 0
    pro = 0
    avg = 0

    for count in range(num_to_input):
        num = get_integer(f"Please enter the number for spot {count + 1}: ")

        if count == 0:
            smallest = num
            largest = num
            pro = num
        else:
            pro *= num

            if num < smallest:
                smallest = num

            if num > largest:
                largest = num

        total += num
       
    avg = total / num_to_input

    print('total', total)
    print('average', avg)
    print('product', pro)
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
