"""Base Hand Class"""

class Hand:
    """Base Hand Class to handle cards in hand."""

    def __init__(self):
        """Initilizer for Hand class."""
        self.hand = []
        self.show_hand = True


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
        hand = self.hand.copy()   
        # loop to check if Ace is in the hand and swaps it to last position. 
        # this ensures the ace gets calculated to ensure it dynamically switches from 1 and 11 properly
        for count in range(len(hand)-1):
            if(hand[count].face == 'Ace'):
                temp = hand[count]
                hand[count] = hand[len(hand) - 1]
                hand[len(hand) - 1] = temp
                print(f'{hand[len(hand) - 1]} swaped with {hand[count]}')
                #break
                # temp = hand[count]
                # hand.remove(hand[count])
                # hand.append(temp)
                # print(temp)

        for card in hand:  # loop to determine the value of cards held in hand
            hand_value += card.determine_card_value(hand_value)

        #print(f'have value: {hand_value}')
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