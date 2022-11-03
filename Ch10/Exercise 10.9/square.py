
from math import sqrt

class Square:

    def __init__(self, side=0):
        self.side = side

    
    @property
    def side(self):
        return self._side


    @side.setter
    def side(self, length):
        if not length >= 0:
            raise ValueError('Length mustbe greater that 0.')
        
        self._side = length

    
    @property
    def perimeter(self):
        return 4 * self.side

    
    @property
    def area(self):
        return (self.side * self.side)


    @property
    def diagonal(self):
        return sqrt(2 * self.side ** 2)