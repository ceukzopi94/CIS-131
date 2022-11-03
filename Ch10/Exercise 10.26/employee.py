"""
Christian Urbanski
CIS 131
10/17/2022
Base Abstract Employee Class
"""

from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta): #must derive from ABCMeta to be classified as a abstract class
    """Base Abstract Employee Class"""

    def __init__(self, first_name, last_name, ssn):
        """Employee Initializer"""
        self._first_name = first_name
        self._last_name = last_name
        self._ssn = ssn

    @property
    def first_name(self):
        """Return the employee first name."""
        return self._first_name

    @property
    def last_name(self):
        """Return the employee last name."""
        return self._last_name

    @property
    def ssn(self):
        """Return the employee social security number."""
        return self._ssn

    @abstractmethod
    def earnings(self):
        raise NotImplementedError('earnings function not implemented in abstract class Employee.')

    def __repr__(self):
        """Return string representation for repr()."""
        return (f'{self.first_name} {self.last_name}\n' +
            f'Social Security Number: {self.ssn}\n')
