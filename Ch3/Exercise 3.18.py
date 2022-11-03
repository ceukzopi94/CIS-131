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
    tri_w = 10

    for row1 in range(tri_w):
        for col1 in range(tri_w):
            print('*' if col1 <= row1 else ' ', end='')

        print('   ', end='')
        
        for col2 in range(tri_w, 0, -1):
            print(' ' if col2 <= row1 else '*', end='')
        
        print('   ', end='')

        for col3 in range(tri_w):
            print(' ' if col3 < row1 else '*', end='')

        print('   ', end='')

        for col4 in range(tri_w, -1, -1):
            print('*' if col4 <= row1 else ' ', end='')
        print()
    print()

    # for row2 in range(tri_w, 0, -1):
    #     for col2 in range(row2):
    #         print('*' if col2 < row2 else ' ', end='')
    #     print()
    # print()

    # for row3 in range(tri_w):
    #     for col3 in range(tri_w):
    #         print(' ' if col3 < row3 else '*', end='')
    #     print()
    # print()

    # for row4 in range(tri_w, 0, -1):
    #     for col4 in range(tri_w+1):
    #         print(' ' if col4 < row4 else '*', end='')
    #     print()
    # print()
    



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
