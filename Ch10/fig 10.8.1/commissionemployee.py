"""CommissionEmployee base class"""
from decimal import Decimal

class CommissionEmployee:
    """An employee who gets paid commission based on gross sales."""

    def __init__(self, first_name, last_name, ssn, gross_sales, commission_rate):
        """Initialize CommissionEmployee's attributes."""
        self._first_name = first_name
        self._last_name = last_name
        self._ssn = ssn
        self._gross_sales = gross_sales # validate via property
        self._commission_rate = commission_rate # validate via property

    
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
    def gross_sales(self):
        """Return the gross sales."""
        return self._gross_sales


    @gross_sales.setter
    def gross_sales(self, sales):
        """Set gross sales or raise Value Error if invalid."""
        if sales < Decimal('0.00'):
            raise ValueError('Gross salesmust be >= 0')

        self._gross_sales = sales


    @property
    def commission_rate(self):
        """Return the commission rate."""
        return self._commission_rate


    @commission_rate.setter
    def commission_rate(self, rate):
        """Set commission rate or raise ValueError if invalid"""
        if not (Decimal('0.0') < rate < Decimal('1.0')):
            raise ValueError('Interest rate must be greater than 0 and less than 1')

        self._commission_rate = rate


    def earnings(self):
        """Calculate earnings."""
        return self.gross_sales * self.commission_rate


    def __repr__(self):
        """Return string representation for repr()."""
        return('CommissionEmployee: ' +
            f'{self.first_name} {self.last_name}\n' +
            f'social security number: {self.ssn}\n' + 
            f'gross sales: {self.gross_sales:.2f}\n' +
            f'commission rate: {self.commission_rate:.2f}')
