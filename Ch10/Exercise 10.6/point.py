"""Point class"""

class Point:

    def __init__(self, x, y):
        self._x = x
        self._y = y


    @property
    def x(self):
        return self._x


    @x.setter
    def x(self, x):
        self._x = x


    @property
    def y(self):
        return self._y


    @y.setter
    def y(self, y):
        self._y = y


    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    
    def __repr__(self):
        """Return a string representation for repr()."""
        return (f'point coordinates: ({self.x}, {self.y})')