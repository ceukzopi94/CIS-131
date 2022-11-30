"""Deck class represents a deck of Cards."""
import random
from card import Card

class DeckOfCards:
    NUMBER_OF_CARDS = 52

    def __init__(self):
        """Initialize the deck."""
        self._current_card = 0
        self._deck = []

        for count in range(DeckOfCards.NUMBER_OF_CARDS):
            self._deck.append(Card(Card.FACES[count % len(Card.FACES)], Card.SUITS[count // len(Card.FACES)]))

    
    def shuffle(self):
        """Shuffle deck."""
        self._current_card = 0
        random.shuffle(self._deck)


    def deal_card(self):
        """Return one Card."""
        try:
            card = self._deck[self._current_card]
            self._current_card += 1
            return card
        except:
            return None


    def __str__(self):
        """Return a string representation of the current _deck."""
        s = ''

        for index, card in enumerate(self._deck):
            s += f'{self._deck[index]:<19}'
            
            if(index + 1) % 4 == 0:
                s += '\n'

        return s