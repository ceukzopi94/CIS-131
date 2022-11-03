"""
Christian Urbanski
CIS 131
10/5/2022
Class Time with read-write properties"""

class Time:
    """Class Time with read-write properties to set and get total seconds since midnight"""

    def __init__(self, time_tuple = (0, 0, 0)):
        """Initialize total second attribute with tuple."""
        self.total_seconds = time_tuple #assigns tuple to total_seconds


    @property
    def total_seconds(self): #getter for total seconds
        """Return the total seconds since midnight."""
        return self._total_seconds


    @total_seconds.setter
    def total_seconds(self, time_tuple): #setter for total seconds
        """Set the total seconds since midnight using a tuple."""

        #checks to make sure the values of tuple are valid
        if not (0 <= time_tuple[0] < 24):
            raise ValueError(f'Hour ({time_tuple[0]}) must be 0-23')

        if not (0 <= time_tuple[1] < 60):
            raise ValueError(f'Minute ({time_tuple[1]}) must be 0-59')

        if not (0 <= time_tuple[2] < 60):
            raise ValueError(f'Second ({time_tuple[2]}) must be 0-59')

        #calculates seconds and sets total seconds
        self._total_seconds = (time_tuple[0] * 60 * 60) + (time_tuple[1] * 60) + time_tuple[2]


    def set_time(self, time_tuple): 
        """Set values of hour, minute, and second from tuple."""
        self.total_seconds = time_tuple


    def __repr__(self):
        """Return Time string for repr()."""
        return(f'Time(total_seconds={self.total_seconds}')


    def __str__(self): 
        """Print Time in total seconds since midnight format."""
        return (f'{self.total_seconds} seconds since midnight.')
