"""
Christian Urbanski
CIS 131
09/06/2022

prompts input for user age 
calculates and displays user's maximum heart rate and range of the user's target heart rate
"""
from random import randrange


STARTING_POS = int(1)
RACE_LEN = int(70)

CONT_STATUS = "CONTINUE"

#put constants here

def main(): 

    #put code here
    game_status = CONT_STATUS

    tortoise_pos = STARTING_POS
    hare_pos = STARTING_POS
    
    print("\nBANG!!!\nAND THEY'RE OFF!!!")

    while game_status == "CONTINUE":

        tortoise_pos += get_tort_move()
        hare_pos += get_hare_move()

        tortoise_pos = check_pos_valid(tortoise_pos)
        hare_pos = check_pos_valid(hare_pos)

        display_race_track()
        display_current_pos(tortoise_pos, hare_pos)

        game_status = get_game_status(tortoise_pos, hare_pos)

    print(game_status)


def get_tort_move():
    """Generates movement for tortoise"""
    move_chance = randrange(1, 11)
    move_num = 0

    if move_chance >= 1 and move_chance <= 5:
        move_num = 3
    elif move_chance > 5 and move_chance <= 8:
        move_num = 1
    else:
        move_num = -6

    return move_num


def get_hare_move():
    """Generates movement for hare"""
    move_chance = randrange(1, 11)
    move_num = 0

    if move_chance >= 1 and move_chance <= 2:
        move_num = 0
    elif move_chance >= 3 and move_chance <= 4:
        move_num = 9
    elif move_chance == 5:
        move_num = -12
    elif move_chance >= 6 and move_chance <= 8:
        move_num = 1
    elif move_chance >= 9 and move_chance <= 10:
        move_num = -2

    return move_num


def check_pos_valid(pos):
    """Checks position and determins if it is valid to Start and Finish"""
    if pos < STARTING_POS:
        pos = STARTING_POS

    if pos >= RACE_LEN:
        pos = RACE_LEN

    return pos


def display_race_track():
    """Displays the race track"""
    for num in range(STARTING_POS, RACE_LEN + 1):
        if num == STARTING_POS:
            print('\nS', end='-')
        elif num == RACE_LEN:
            print('F')
        else:
            print(end='-')


def display_current_pos(t_pos, h_pos):
    """Displays current position of racers"""
    for spot in range(STARTING_POS, RACE_LEN + 1):
        if t_pos == spot and h_pos == spot:
            print('OUCH!', end='_')
        elif t_pos == spot:
            if spot == RACE_LEN:
                print('T')
            else:
                print('T', end='_')
        elif h_pos == spot:
            if spot == RACE_LEN:
                print('H')
            else:
                print('H', end='_')
        else:
            print(end='_')
    
    print('')


def get_game_status(t_pos, h_pos):
    """Gets the current game status"""

    if t_pos == RACE_LEN and h_pos == RACE_LEN:
        return "It's a tie..."

    if t_pos == RACE_LEN:
        return "The Tourtoise Won!!!"

    if h_pos == RACE_LEN:
        return "The hare won... Yuck!"

    return CONT_STATUS

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
