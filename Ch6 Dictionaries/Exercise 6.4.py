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
    first_set = {1, 2, 4, 8, 16}
    second_set = {1, 4, 16, 64, 256}

    print(sorted(first_set.union(second_set)))
    print(sorted(first_set.intersection(second_set)))
    print(sorted(first_set.difference(second_set)))
    print(sorted(first_set.symmetric_difference(second_set)))
    print(first_set.isdisjoint(second_set))

    first_dic = {1: 1, 2: 2, 3: 4, 4: 8, 5: 16}
    second_dic = {1: 1, 2: 4, 3: 16, 4: 64, 5: 256}

    total_dic = first_dic.update(second_dic)

    print(total_dic)
    



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
