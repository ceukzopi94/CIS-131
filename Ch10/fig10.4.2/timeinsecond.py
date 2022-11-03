"""
Christian Urbanski
CIS 131
10/5/2022
Class Time with read-write properties"""


class Time:
    """Class Time with read-write properties."""

    def __init__(self, hour=0, minute=0, second=0):
        """Initialize each attribute."""
        self.hour = hour # 0-23
        self.minute = minute # 0-59
        self.seconds = second # 0-59


    @property
    def total_seconds(self):
        """Return the total seconds since midnight."""
        return self._total_seconds


    @total_seconds.setter
    def hour(self, hour):
        """Set the hour."""
        if not (0 <= hour < 24):
            raise ValueError(f'Hour ({hour}) must be 0-23')

        self._total_seconds = (hour * 60 * 60)


    @total_seconds.setter
    def minute(self, minute):
        """Set the minute"""
        if not (0 <= minute < 60):
            raise ValueError(f'Minute ({minute}) must be 0-59')

        self._total_seconds += (minute * 60)


    @total_seconds.setter
    def seconds(self, second):
        """Set the second"""
        if not (0 <= second < 60):
            raise ValueError(f'Second ({second}) must be 0-59')

        self._total_seconds += second


    def set_time(self, hour=0, minute=0, second=0):
        """Set values of hour, minute, and second."""
        self.hour = hour
        self.minute = minute
        self.seconds = second


    def __repr__(self):
        """Return Time string for repr()."""
        return(f'Time(hour={self.hour}, minute={self.minute}, second={self.seconds}')


    def __str__(self):
        """Return Time string displaying time since midnight."""
        return (f'{self.total_seconds} seconds since midnight.')
