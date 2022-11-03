"""SalariedCommissionEmployee derived from CommossionEmployee"""
from logging.config import valid_ident
from commissionemployee import CommissionEmployee
from decimal import Decimal

class SalariedCommissionEmployee(CommissionEmployee):
    """An employee who getspaid a salary plus commission based on gross sales"""

    def __init__(self, first_name, last_name, ssn, gross_sales, commission_rate, base_salary):
        """Initialize SalariedCommissionEmployee's attributes"""
        super().__init__(first_name, last_name, ssn, gross_sales, commission_rate)

        self.base_salary = base_salary # validate via property


    @property
    def base_salary(self):
        """Return the base salary."""
        return self._base_salary

    
    @base_salary.setter
    def base_salary(self, salary):
        """Set base salary or raise ValueError if invalid"""
        if salary < Decimal('0.00'):
            raise ValueError('Base salary mustbe >= to 0.')

        self._base_salary = salary


    def earnings(self):
        """Calculate earnings."""
        return super().earnings() + self.base_salary


    def __repr__(self):
        """Return string representation for repr()."""
        return ('Salaried' + super().__repr__() +
            f'\nbase salary: {self.base_salary:.2f}')
