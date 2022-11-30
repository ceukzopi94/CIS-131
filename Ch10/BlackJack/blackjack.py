"""
Christian Urbanski
CIS 131
09/06/2022

This program is the game of blackjack.
"""

from deck import DeckOfCards
from playerhand import PlayerHand
from dealerhand import DealerHand

deck_of_carks = DeckOfCards()

player_hand = PlayerHand()
dealer_hand = DealerHand()

PLAY_GAME_MSG = '\nWould you like to play a hand of Black Jack? (y/n) '
END_GAME_MSG = '\nThank you for playing Black Jack!\n'

ENTER_BET_MSG = '\nHow much would you like to bet? (Enter 0 stop hand) '

DEALER_WINS_STATUS = 'Dealer Wins.'
DEALER_BLACKJACK = 'Dealer has blackjack.'
DEALER_BUST = 'Dealer Bust!'

PLAYER_WINS_STATUS = 'Player Wins!'
PLAYER_BLACKJACK = 'Player has blackjack.'
PLAYER_BUST = 'Player Bust...'
PLAYER_H_S_MSG = '\nHit (h) or Stand (s): '

PUSH_STATUS = 'Push...'
CONTINUE_STATUS = 'Continue'

BLACKJACK_MULTIPLIER = 1.5
SENTINAL_VALUE = 0

def main(): 
    pass


def play_blackjack(machine_credits):
    """Function to control the game of blackjack"""

    #ask to play a game of BJ
    #play_game = get_yes_or_no(PLAY_GAME_MSG)

    print(f'Machine Credits: {machine_credits.balance}')
    bet = take_bets(machine_credits)

    while (bet > 0):
        start_new_hand()  # call to start new game

        #take bets
        #bet = take_bets(machine_credits)

        # if(bet == 0):
        #     play_game = get_yes_or_no(PLAY_GAME_MSG)
        #     return

        deal_cards()

        player_hand.display_hand()
        print('')
        dealer_hand.display_hand(False)
        print('')

        #check for blackjack
        natural_blackjack = determine_blackjack(dealer_hand, player_hand)

        if natural_blackjack == None:
            play_player_hand(player_hand)
            play_dealer_hand(dealer_hand)

        player_hand.display_hand()
        dealer_hand.display_hand(True)

        winner = determine_winner(player_hand, dealer_hand)

        payout_player(winner, bet, machine_credits)

        #play_game = get_yes_or_no(PLAY_GAME_MSG)
        print(f'Machine Credits: {machine_credits.balance}')
        bet = take_bets(machine_credits)

    play_game = get_yes_or_no(PLAY_GAME_MSG)

    if(play_game):
        play_blackjack(machine_credits)

    print(END_GAME_MSG)

    return machine_credits


def take_bets(machine_credits):
    """Function to take bet of the player"""
    if(machine_credits.balance == 0):
        print('No Credits')
        machine_credits.get_deposit()

    bet = get_integer(ENTER_BET_MSG)

    while(invalid_bet(machine_credits, bet)):
        bet = get_integer(ENTER_BET_MSG)

    return bet


def invalid_bet(machine_credits, bet):
    """Function to determine if bet is valid or not."""
    if(bet == SENTINAL_VALUE):
        return False

    if (bet > machine_credits.balance):
        print('Not Enough Credits.')
        print(f'Current Credits: {machine_credits.balance}')
        machine_credits.get_deposit()
        return True


def get_deposit(machine_credits):
    """Function to get a deposit from the player."""
    is_depositing = get_yes_or_no('Would you like to deposit credits into the machine? (y/n) ')

    if (is_depositing):
        machine_credits.deposit(get_positive_int('Enter amount to deposit: '))


def start_new_hand(): #refactor to do more or get rid of
    """Function to start a new hand of blackjack."""
    global player_hand
    global dealer_hand

    player_hand = PlayerHand()
    dealer_hand = DealerHand()

    deck_of_carks.shuffle()


def deal_cards():
    """Function deals cards in sequence to player than dealer."""
    players = [player_hand, dealer_hand]
    num_cards_to_deal = 2

    for count in range(num_cards_to_deal): #loops to deal the correct amount of cards to players
        for player in players: # loop to deal a card to each player
            card = deck_of_carks.deal_card()
            player.add_card(card)


# def determine_hand_value(hand):
#     """Return the value of the hand."""
#     hand_value = 0

#     for card in hand.hand: #loop to determine the value of cards held in hand
#         hand_value += determine_card_value(card, hand_value)

#     return hand_value


# def determine_card_value(card, hand_value):
#     """Determine the value of the card face."""
#     if card.face == 'Ace':
#         if hand_value > 21: #makes ace value dynamic based on best possible option
#             return 1

#         return 11

#     if card.face == 'Jack' or card.face == 'Queen' or card.face == 'King': #assigns face card values
#         return 10

#     return int(card.face) 


def determine_blackjack(dealer_hand, player_hand):
    """Determines if players have natural blackjack."""
    if dealer_hand.determine_hand_value() == 21: 
        if player_hand.determine_hand_value() == 21:
            return PUSH_STATUS

        return DEALER_BLACKJACK

    if player_hand.determine_hand_value() == 21:
        return PLAYER_BLACKJACK

    return None


def play_player_hand(player_hand):
    """Function to player to play their hand."""
    player_can_hit = get_player_game_state(PLAYER_H_S_MSG, player_hand)

    while player_can_hit: #loops to control player controls in game
        player_hand.add_card(deck_of_carks.deal_card())
        player_hand.display_hand()

        player_can_hit = get_player_game_state(PLAYER_H_S_MSG, player_hand)


def play_dealer_hand(dealer_hand):
    """Determines statues of dealer hand and plays out until conditions hit."""
    dealer_hand.show_hand = True

    hand_value = dealer_hand.determine_hand_value()

    if hand_value < 17:
        dealer_hand.add_card(deck_of_carks.deal_card()) 

        #recursive call to play out the dealer hand until hand valueis greater than 17
        play_dealer_hand(dealer_hand) 


def determine_winner(player_hand, dealer_hand):
    """Function to determine the winner and display winnning message"""
    if (determine_hand_bust(player_hand) and determine_hand_bust(dealer_hand)):
        return (PUSH_STATUS)
    
    if(determine_hand_bust(dealer_hand)):
        return (PLAYER_WINS_STATUS)

    if(determine_hand_bust(player_hand)):
        return (DEALER_WINS_STATUS)

    if (player_hand.determine_hand_value() == dealer_hand.determine_hand_value()):
        return (PUSH_STATUS)

    if (dealer_hand.determine_hand_value() > player_hand.determine_hand_value()):
        return (DEALER_WINS_STATUS)

    if (dealer_hand.determine_hand_value() < player_hand.determine_hand_value()):
        return (PLAYER_WINS_STATUS)


def payout_player(winner, bet, machine_credits):
    """Function to payout the player."""
    global player_hand

    if(winner == PLAYER_WINS_STATUS):
        if(player_hand.determine_hand_value() == 21 and len(player_hand.hand) <= 2):
            machine_credits.deposit(bet * BLACKJACK_MULTIPLIER)
            print(f'BLACKJACK!!! Player wins {bet * BLACKJACK_MULTIPLIER}')
            return
        machine_credits.deposit(bet)
        print({winner})
        print(f'Credits Won: {bet}')
        return

    if(winner == DEALER_WINS_STATUS):
        machine_credits.withdraw(bet)
        print('Dealer Wins...')
        print(f'Player loses {bet}')
        return

    if(winner == PUSH_STATUS):
        print('Player pushes the dealer.')
        print('No Credits Awarded or Deducted.')
        return


def get_player_game_state(msg, hand):
    """Function to control the player choice."""
    if determine_hand_bust(hand):
        return False

    if hand == 21:
        return False

    choice = get_hit_or_stand(msg)

    return choice


def determine_hand_bust(hand):
    """Function to determine if the hand bust or not"""

    if hand.determine_hand_value() > 21:
        return True

    return False


def get_hit_or_stand(message, prompt="none"):
    """Function to get the hit or stand choice from the player."""
    while True:
        new_value = get_string(message, prompt)
        new_value = new_value.lower()
        if new_value == "h" or new_value == "hit":
            return True
        if new_value == "s" or new_value == "stand":
            return False
        print('Error: invalid value entered. Please enter Hit (h) or Stand (s)')


#---------------------------------------------------------------------------------
def get_positive_int(msg):
    """Function to get positive number."""
    number = get_integer(msg)

    while(number < 0):
        print('Please enter positive number.')
        number = get_integer(msg)

    return number


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
