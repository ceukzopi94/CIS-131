"""
Christian Urbanski
CIS 131
09/06/2022

prompts input for user age 
calculates and displays user's maximum heart rate and range of the user's target heart rate
"""
from collections import Counter
from multiprocessing.reduction import duplicate
#put constants here

letters_used = {}

def main(): 
    #put code here
    text = ('this is a sample text with several words '
            'this IS more sample text with some different Words xzzz')

    text = text.lower()

    counter = Counter(text.split())
    duplicate_word = ''

    for word, count in sorted(counter.items()):
        if count > 1:
            duplicate_word += word
            print(f'{word:<12}{count}')
    
    build_letters_used(text)

    for letter, count in sorted(letters_used.items()):
        print(f'{letter:<5}{count}')


def build_letters_used(lst):
    words = lst

    for letter in words:
        if letter == ' ':
            continue

        if letter in letters_used:
            letters_used[letter] += 1
        else:
            letters_used[letter] = 1

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