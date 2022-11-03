"""
Christian Urbanski
CIS 131
09/06/2022

prompts input for user age 
calculates and displays user's maximum heart rate and range of the user's target heart rate
"""

#put constants here
SENTINEL = -1
-1
def main(): 
    #put code here
    
    total = 0 #sum of grades
    grade_counter = 0 #num of grades entered

    with open('grades.txt', mode = 'w') as grades: #opens the grades.txt, if no file found, it will create one 
        grade = get_integer('Enter Grade, -1 to end: ')

        while grade != SENTINEL:
            grades.write(f'{grade}\n')

            total += grade
            grade_counter += 1

            grade = get_integer('Enter Grade, -1 to end: ')

        if grade_counter != 0:
            average = total / grade_counter
            print(f'Class Average: {average:.2f}')
        else:
            print('No grades were entered.')


    



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
