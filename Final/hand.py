"""Base Hand Class"""

class Hand:
    """Base Hand Class to handle cards in hand."""

    def __init__(self):
        """Initilizer for Hand class."""
        self.hand = []


    @property
    def hand(self):
        """Return the hand list."""
        return self._hand


    @hand.setter
    def hand(self, hand):
        """Set the hand."""
        self._hand = hand


    def set_hand(self, hand):
        """Set the hand using a list."""
        self.hand = hand


    def add_card(self, card):
        """Add card to the hand."""
        self.hand.append(card)


    def determine_hand_value(self):
        """Return the value of the hand."""
        hand_value = 0

        for card in self.hand:  # loop to determine the value of cards held in hand
            hand_value += card.determine_card_value(hand_value)

        return hand_value


    def display_hand(self, display_hand_value=True):
        """Function to display the hand and hand value.\n
        display_hand_value = True by defualt\n
        set false to hide hand value."""

        print('*' * 20)

        print(self)

        if display_hand_value:
            hand_value = self.determine_hand_value()
            print(f'Hand Value: {hand_value}')

            if(hand_value > 21):
                print('')
                print('Bust...')
            
            if(hand_value == 21 and len(self.hand) <= 2):
                print('')
                print('Blackjack!')

        

        print('*' * 20)


    def __str__(self):
        """Return a string representation of the current hand."""
        hand_string = ''

        for index, card in enumerate(self.hand):
            hand_string += f'{self.hand[index]:<19}'

        return hand_string