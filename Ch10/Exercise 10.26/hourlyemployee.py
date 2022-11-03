"""
Christian Urbanski
CIS 131
10/17/2022
Concrete Class SalariedEmployee
"""

from employee import Employee

class HourlyEmployee(Employee):
    """Concrete Sub-class SalariedEmployee."""

    def __init__(self, first_name, last_name, ssn, hours, wages):
        """Initializer for concrete sub-class SalariedEmployee"""
        super().__init__(first_name, last_name, ssn) #calls base class init

        self.hours = hours
        self.wages = wages

    @property
    def hours(self):
        """Return the weekly salary of HourlyEmployee."""
        return self._hours

    @hours.setter
    def hours(self, hours):
        """Set the weekly salary of HourlyEmployee"""
        if not hours in range(0, 168):
            raise ValueError('Hours must be between 0 and 168.')

        self._hours = hours

    @property
    def wages(self):
        """Return the wages of HourlyEmployee"""
        return self._wages

    @wages.setter
    def wages(self, wages):
        """Set the wages for HourlyEmployee."""
        if not wages >= 0:
            raise ValueError('Wages must be be greater than or equal to 0.')

        self._wages = wages

    def earnings(self):
        """Return the earnings of HourlyEmployee."""
        return self.hours * self.wages

    def __repr__(self):
        """Return string representation for repr()."""
        return ('HourlyEmployee:\n' + 
            super().__repr__() +
            f'Hours worked: {self.hours} hours' + 
            f'\nWages: ${self.wages:.2f} per hour.')
