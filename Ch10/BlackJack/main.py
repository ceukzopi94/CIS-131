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

DEALER_WINS_STATUS = 'Dealer Wins.'
DEALER_BLACKJACK = 'Dealer has blackjack.'
DEALER_BUST = 'Dealer Bust!'

PLAYER_WINS_STATUS = 'Player Wins!'
PLAYER_BLACKJACK = 'Player has blackjack.'
PLAYER_BUST = 'Player Bust...'
PLAYER_H_S_MSG = '\nHit (h) or Stand (s): '

PUSH_STATUS = 'Push...'
CONTINUE_STATUS = 'Continue'

def main(): 
    deck_of_carks.shuffle()

    start_new_hand() #call to start new game

    player_hand_value = determine_hand_value(player_hand)
    
    display_hand(player_hand)
   
    print('')

    dealer_hand_value = determine_hand_value(dealer_hand)
    display_hand(dealer_hand, False)

    print('')
  
    #check for blackjack
    game_status = determine_blackjack(dealer_hand, player_hand)
    
    print(f'Game Status: {game_status}')

    if game_status == CONTINUE_STATUS:
        player_hand_value = play_player_hand(player_hand)
        dealer_hand_value = play_dealer_hand(dealer_hand)

    display_hand(player_hand)
    display_hand(dealer_hand)

    # print(f'Player Hand Value: {player_hand_value}')
    # print(f'Dealer Hand Value: {dealer_hand_value}')

    #ask player to hit, stand

    #loop if hit
    #check for bust
    #ask player to hit, stand


def start_new_hand(): #refactor to do more or get rid of
    """Function to start a new hand of blackjack."""
    #take bets

    deals_cards()


def deals_cards():
    """Function deals cards in sequence to player than dealer."""
    players = [player_hand, dealer_hand]
    num_cards_to_deal = 2

    for count in range(num_cards_to_deal): #loops to deal the correct amount of cards to players
        for player in players: # loop to deal a card to each player
            cards = deck_of_carks.deal_card()
            player.add_card(cards)


def determine_hand_value(hand):
    """Return the value of the hand."""
    hand_value = 0

    for card in hand.hand: #loop to determine the valueof cards held in hand
        hand_value += determine_card_value(card, hand_value)

    return hand_value


def determine_card_value(card, hand_value):
    """Determine the value of the card face."""
    if card.face == 'Ace':
        if hand_value > 21: #makes ace value dynamic based on best possible option
            return 1

        return 11

    if card.face == 'Jack' or card.face == 'Queen' or card.face == 'King': #assigns face card values
        return 10

    return int(card.face) 


def determine_blackjack(dealer_hand, player_hand):
    """Determines if players have natural blackjack."""
    if dealer_hand == 21: 
        if player_hand == 21:
            return PUSH_STATUS

        return DEALER_BLACKJACK

    if player_hand == 21:
        return PLAYER_BLACKJACK

    return CONTINUE_STATUS


def play_player_hand(player_hand):
    """Function to player to play their hand."""
    hand_value = determine_hand_value(player_hand)
    player_can_hit = get_player_game_state(PLAYER_H_S_MSG, hand_value)

    while player_can_hit: #loops to control player controls in game
        player_hand.add_card(deck_of_carks.deal_card())
        
        hand_value = determine_hand_value(player_hand)

        display_hand(player_hand)

        # if determine_hand_bust(hand_value):
        #     continue

        player_can_hit = get_player_game_state(PLAYER_H_S_MSG, hand_value)

    return hand_value


def play_dealer_hand(dealer_hand):
    """Determines statues of dealer hand and plays out until conditions hit."""
    dealer_hand.show_hand = True

    hand_value = determine_hand_value(dealer_hand)

    while hand_value < 17:
        dealer_hand.add_card(deck_of_carks.deal_card()) 
        hand_value = determine_hand_value(dealer_hand)

    return hand_value


def determine_hand_bust(hand_value):
    """Function to determine if the hand bust or not"""

    if hand_value > 21:
        return True

    return False


def get_player_game_state(msg, hand_value):
    """Function to control the player choice."""
    if determine_hand_bust(hand_value):
        return False

    if hand_value == 21:
        return False

    choice = get_hit_or_stand(msg)

    return choice


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


def display_hand(hand, display_hand_value = True):
    """Function to display the hand and hand value.\n
    display_hand_value = True by defualt\n
    set false to hide hand value."""

    print('*' * 20)

    print(hand)

    if display_hand_value:
        print(f'Hand Value: {determine_hand_value(hand)}')

    print('*' * 20)


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
