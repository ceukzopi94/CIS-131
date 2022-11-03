"""
Christian Urbanski
CIS 131
09/06/2022

prompts input for user age 
calculates and displays user's maximum heart rate and range of the user's target heart rate
"""
import random

#put constants here

def main(): 
    #put code here
    #dictionsteofus states
    state_capitals = {'Alabama':	'Montgomery',
                      'Alaska':	'Juneau',
                      'Arizona':	'Phoenix',
                      'Arkansas':	'Little Rock',
                      'California':	'Sacramento',
                      'Colorado':	'Denver',
                      'Connecticut':	'Hartford',
                      'Delaware':	'Dover',
                      'Florida':	'Tallahassee',
                      'Georgia':	'Atlanta',
                      'Hawaii':	'Honolulu',
                      'Idaho':	'Boise',
                      'Illinois':	'Springfield',
                      'Indiana':	'Indianapolis',
                      'Iowa':	'Des Moines',
                      'Kansas':	'Topeka',
                      'Kentucky':	'Frankfort',
                      'Louisiana':	'Baton Rouge',
                      'Maine':	'Augusta',
                      'Maryland':	'Annapolis',
                      'Massachusetts':	'Boston',
                      'Michigan':	'Lansing',
                      'Minnesota':	'Saint Paul',
                      'Mississippi':	'Jackson',
                      'Montana':	'Helena',
                      'Nebraska':	'Lincoln',
                      'Nevada':	'Carson City',
                      'New Hampshire':	'Concord',
                      'New Jersey':	'Trenton',
                      'New Mexico':	'Santa Fe',
                      'New York':	'Albany',
                      'North Carolina':	'Raleigh',
                      'North Dakota':	'Bismarck',
                      'Ohio':	'Columbus',
                      'Oklahoma':	'Oklahoma City',
                      'Oregon':	'Salem',
                      'Pennsylvania':	'Harrisburg',
                      'Rhode Island':	'Providence',
                      'South Carolina':	'Columbia',
                      'South Dakota':	'Pierre',
                      'Tennessee':	'Nashville',
                      'Texas':	'Austin',
                      'Utah':	'Salt Lake City',
                      'Vermont':	'Montpelier',
                      'Virginia':	'Richmond',
                      'Washington':	'Olympia',
                      'West Virginia':	'Charleston',
                      'Wisconsin':	'Madison',
                      'Wyoming':	'Cheyenne'}

    incorret_guesses = 0
    corret_guesses = 0
    cont = True

    while(cont):
        state = random.choice(list(state_capitals))

        user_guess = get_string(f'\nEnter the capital of {state}: ')

        while user_guess != state_capitals[state]:
            incorret_guesses += 1

            print('Wrong... try again...\n')
            user_guess = get_string(f'Enter the capital of {state}: ')

        corret_guesses += 1

        print(f'\nCorrect!\nIt took you {incorret_guesses} times to get it right.')
        print(f'You have guessed {corret_guesses} capitals right.')

        cont = get_yes_or_no('\nDo you want to play again? (y / n)')


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
