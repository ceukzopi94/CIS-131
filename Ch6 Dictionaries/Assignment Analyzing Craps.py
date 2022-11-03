"""
Christian Urbanski
CIS 131
09/06/2022

plays the game of craps
counts how many times player wins/losses on specific rolls
displays the percentage of wins/losses
also displays table of how many times the game ended on specific rolls
"""
import random

#put constants here
WIN_STATUS = 'WIN'
LOSE_STATUS = 'LOSE'
CONTINUE_STATUS = 'CONTINUE'
NUM_GAMES_TO_PLAY = 1000 #how many times the game wil be played

#global variables
point_num = 0
times_dice_rolled = 0

#dictionaries
wins = {}
losses = {}
total_win_loss_rolls = {}

def main():
    """Main function where program is handled"""
    for game_num in range(NUM_GAMES_TO_PLAY):
        play_single_crap_game()
        
    total_win_lose = get_total_win_loss()

    build_win_loss_dictionary()

    display_win_lose_percentages(total_win_lose)
    display_roll_percentages_table()
    

def play_single_crap_game():
    """Plays a single game of craps until player wins or losses"""
    print('\n---------------------')

    dice = roll_dice()   
    display_dice(dice)

    game_status = determine_game_statues(dice)
     
    while game_status == CONTINUE_STATUS:
        dice = roll_dice() 
        display_dice(dice)

        game_status = determine_game_statues(dice)
        
    display_win_lose_msg(game_status)

    reset_game()


def roll_dice():
    """Roll two dice and return their values as tuple"""
    global times_dice_rolled
    times_dice_rolled += 1

    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)

    return (die_1, die_2)


def determine_game_statues(dice):
    """Determines the game status depending on sum of dice. Returns win, lose or continue status"""
    total = sum(dice)

    if times_dice_rolled == 1: #check to see is this is the first roll
        if total in (7, 11):
            return WIN_STATUS

        if total in (2, 3, 12):
            return LOSE_STATUS

        else:
            global point_num
            point_num = total
            print(f'Point: {point_num}')

            return CONTINUE_STATUS

    else: #handles every roll after the first
        if total == point_num:
            return WIN_STATUS

        elif total == 7:
            return LOSE_STATUS

        return CONTINUE_STATUS


def get_total_win_loss():
    """Function to get the total win/lose in a tuple"""
    total_wins = sum(list(wins.values()))
    total_losses = sum(list(losses.values()))

    return(total_wins, total_losses)


def increment_dictionary_value(dic):
    """Function to increment passed in dictionary depending if key already exist\n
    If it does not exist, it inserts values at corresponding position."""
    if times_dice_rolled in dic:
        dic[times_dice_rolled] += 1
    else:
        dic[times_dice_rolled] = 1


def build_win_loss_dictionary():
    """Function to build the win/lose dictionary"""

    dice_roll_set = list(wins.keys()) + list(losses.keys()) #makes a list of keys used in dictionaries
    dice_roll_set = set(dice_roll_set) #creates set of keys for iteration for dictionary assignment

    for rolls in dice_roll_set:
        if rolls in (losses.keys()) and rolls in (wins.keys()):
            total_win_loss_rolls[rolls] = wins[rolls] + losses[rolls]

        elif rolls in (losses.keys()):
            total_win_loss_rolls[rolls] = losses[rolls]

        elif rolls in (wins.keys()):
            total_win_loss_rolls[rolls] = wins[rolls]


def  display_dice(dice):
    """Function to display the dice rolled"""
    die_1, die_2 = dice

    print('\nDie 1 - Die 2 - Total')
    print(f'{die_1:>3}{die_2:>8}{sum(dice):>8}')


def display_win_lose_msg(status):
    """Displays the win lose message and calls to update dictionary"""
    if status == WIN_STATUS:
        print(f'Player wins after {times_dice_rolled} rolls!')

        increment_dictionary_value(wins)

    else: 
        print(f'Player lost after {times_dice_rolled} rolls')

        increment_dictionary_value(losses)


def display_win_lose_percentages(win_lose):
    """Function to display the win/lose percentages"""
    total_wins, total_losses = win_lose

    win_percent = calc_percent(total_wins, NUM_GAMES_TO_PLAY)
    lose_percent = calc_percent(total_losses, NUM_GAMES_TO_PLAY)

    print(f'Percentage of wins: {win_percent:.1f}%')
    print(f'Percentage of losses: {lose_percent:.1f}%')
    print('Percentage of wins/losses based on total number of rolls')


def display_roll_percentages_table():
    """Displays percentage table of rolls"""

    cumulative_percentage = 0.0

    print(f'\nRolls  % Resolved  Cumulative %')

    for rolls in (total_win_loss_rolls.keys()):

        resolved_percent = calc_percent(total_win_loss_rolls[rolls], NUM_GAMES_TO_PLAY)
        cumulative_percentage += resolved_percent

        print(f'{rolls:>5}{(resolved_percent):>12.2f}{cumulative_percentage:14.2f}')


def calc_percent(num1, num2):
    """Calculates percentage of passed in values"""
    return (num1 / num2) * 100

         
def reset_game():
    """Function to reset game to initial values"""
    global times_dice_rolled
    global point_num

    times_dice_rolled = 0
    point_num = 0

    print('---------------------')

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
