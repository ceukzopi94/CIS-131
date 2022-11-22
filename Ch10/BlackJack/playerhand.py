"""PlayerHand Sub Class"""

from hand import Hand

class PlayerHand(Hand):
    """PlayerHand Sub Class"""

    def __init__(self):
        super().__init__()

    def __str__(self):
        """Return a string representation of the current hand."""
        hand_string = 'Player Hand:\n\n'

        for index, card in enumerate(self.hand):
            hand_string += f'{self.hand[index]:<19}'

        return hand_string