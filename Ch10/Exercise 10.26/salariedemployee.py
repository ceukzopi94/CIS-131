"""
Christian Urbanski
CIS 131
10/17/2022
Concrete Class SalariedEmployee
"""

from employee import Employee

class SalariedEmployee(Employee):
    """Concrete Sub-class SalariedEmployee."""

    def __init__(self, first_name, last_name, ssn, weekly_salary):
        """Initializer for concrete sub-class SalariedEmployee"""
        super().__init__(first_name, last_name, ssn) #calls base class init

        self.weekly_salary = weekly_salary

    @property
    def weekly_salary(self):
        """Return the weekly salary of SalariedEmployee."""
        return self._weekly_salary

    @weekly_salary.setter
    def weekly_salary(self, weekly_salary):
        """Set the weekly salary of SalariedEmployee"""
        if not weekly_salary >= 0:
            raise ValueError('Salary must be greater than or equal to 0.')

        self._weekly_salary = weekly_salary

    def earnings(self):
        """Return the earnings of HourlyEmployee."""
        return self.weekly_salary

    def __repr__(self):
        """Return string representation for repr()."""
        return ('SalariedEmployee:\n' + 
            super().__repr__() +
            f'Weekly salary: ${self.weekly_salary:,.2f}')
