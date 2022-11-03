#put constants here
SIZE = 7


def main(): 
    #put code here
    user_num = get_integer('Please enter a 5 digit number: ')

    first_num = user_num // 10000
    remain_num = user_num % 10000

    second_num = remain_num // 1000
    remain_num = remain_num % 1000

    third_num = remain_num // 100
    remain_num = remain_num % 100

    forth_num = remain_num // 10
    remain_num = remain_num % 10

    fifth_num = remain_num 
    
    print(first_num, ' ', second_num , ' ', third_num, ' ', forth_num, ' ', fifth_num)

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
