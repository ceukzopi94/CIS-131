"""Circle class"""
from point import Point

class Circle:
    
    def __init__(self, radius):
        self._radius = radius
        self._point = Point(0, 0)


    @property
    def radius(self):
        """Return the radius of the circle."""
        return self._radius


    @property
    def point(self):
        """Return the center point of the circle."""
        return self._point


    def move(self, x, y):
        """Move the circle."""
        self.point.move(x, y)


    def __repr__(self):
        """Return a string representation for repr()."""
        return ('\nCircle:\n' + 
            f'radius: {self.radius}\n' +
            f'{self.point}')