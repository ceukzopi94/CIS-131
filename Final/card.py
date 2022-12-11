"""

Christian Urbanski
12/06/2022
CIS 131
Card class that represents a playing card and its image file name
"""

import os

class Card:
    FACES = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']


    def __init__(self, face, suit):
        """Initialize a Card with a face and suit"""
        self.face = face
        self.suit = suit
        self.path = os.path.dirname(os.path.abspath(__file__)) 
        self.image_path = "{}/card_images/{}.png".format(self.path, self.image_name)
        self.back_image = "{}/card_images/back_of_card.png".format(self.path)


    @property
    def face(self):
        """Return the Card's self._face value"""
        return self._face

    @face.setter
    def face(self, face):
        """Set the Card's face value."""
        self._face = face


    @property
    def suit(self):
        """Return the Card's self._suit value"""
        return self._suit

    @suit.setter
    def suit(self, suit):
        """Set the Card's face value."""
        self._suit = suit


    @property
    def image_name(self):
        """Return the Card's image file name"""
        return str(self).replace(' ','_') 


    @property
    def image_path(self):
        """Retrun the Card's image path."""
        return self._image_path

    @image_path.setter
    def image_path(self, path):
        """Set Card's image path."""
        self._image_path = path

    @property
    def back_image(self):
        """Return the Card's back image path"""
        return self._back_image

    @back_image.setter
    def back_image(self, path):
        """Set Card's image path."""
        self._back_image = path


    # def get_image_path(self):
    #     """Function to return the image path of the card"""



    def determine_card_value(self, hand_value):
        """Determine the value of the card face."""
        if self.face == 'Ace':
            if hand_value + 11 > 21:  # makes ace value dynamic based on best possible option
                #print(f'ace has value 1') #debug purposses
                return 1
            #print(f'ace has value 11') #debug purposses
            return 11

        if self.face == 'Jack' or self.face == 'Queen' or self.face == 'King':  # assigns face card values
            return 10

        return int(self.face)


    def __repr__(self):
        """Return string representation for repr()."""
        return f"Card(face='{self.face}', suit='{self.suit}'"


    def __str__(self) -> str:
        """Return string representation for str()."""
        return f'{self.face} of {self.suit}'


    def __format__(self, format):
        """Return formatted string representation for str()."""
        return f'{str(self):{format}}'