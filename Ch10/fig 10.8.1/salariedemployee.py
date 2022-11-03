"""SalariedEmployee base class"""

from calendar import week
from decimal import Decimal


class SalariedEmployee:


    def __init__(self, first_name, last_name, ssn, weekly_pay):
        """Initialize CommissionEmployee's attributes."""
        self._first_name = first_name
        self._last_name = last_name
        self._ssn = ssn
        self._weekly_pay = weekly_pay


    @property
    def first_name(self):
        """Return the first name."""
        return self._first_name


    @property
    def last_name(self):
        """Return the last name."""
        return self._last_name


    @property
    def ssn(self):
        """Return the ssn."""
        return self._ssn


    @property
    def weekly_pay(self):
        """Return the weekly pay."""
        return self._weekly_pay


    @weekly_pay.setter
    def weekly_pay(self, pay):
        """Set weekly pay or raise Value Error if invalid."""
        if pay < Decimal('0.00'):
            raise ValueError('Weekly pay must be >= 0')

        self._weekly_pay = pay


    def earnings(self):
        """Calculate earnings."""
        return self.weekly_pay * 52


    def __repr__(self):
        """Return string representation for repr()."""
        return ('SalariedEmployee: ' +
                f'{self.first_name} {self.last_name}\n' +
                f'social security number: {self.ssn}\n' +
                f'weekly pay: {self.weekly_pay:.2f}')
