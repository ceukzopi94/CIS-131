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

    def __str__(self):
        """Return a string representation of the current hand."""
        hand_string = ''

        for index, card in enumerate(self.hand):
            hand_string += f'{self.hand[index]:<19}'

        return hand_string