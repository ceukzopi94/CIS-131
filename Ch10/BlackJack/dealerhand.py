"""Hand Subclass DealerHand"""
from hand import Hand

class DealerHand(Hand):
    """DealerHand Sublass to handle dealer hand."""

    def __init__(self):
        super().__init__()

        self.show_hand = False

    @property
    def show_hand(self):
        """Return bool to show hand"""
        return self._show_hand

    @show_hand.setter
    def show_hand(self, show):
        """Set bool to show hand"""
        self._show_hand = show

    def __str__(self):
        """Return a string representation of the dealer hand."""
        hand_string = 'Dealer Hand:\n'

        if self.show_hand:
            for index, card in enumerate(self.hand):
                hand_string += f'{self.hand[index]:<19}'
        else:
            hand_string += (f'{"X" * 13}      {self.hand[1]:<19}')

        return hand_string

    # def __repr__(self):
    #     """Return string rep of dealer hand."""
    #     if self.show_hand:
    #         #shows hand if show_hand is true
    #         return (f'First Card: {self.first_card} ' +
    #                 f'Second Card: {self.second_card}')

    #     return (f'First Card: *********** ' +
    #             f'Second Card: {self.second_card}')
