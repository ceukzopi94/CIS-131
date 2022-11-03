

from decimal import Decimal


class Invoice:
    """Invoice class with read-write properties for store items."""
    def __init__(self, part_number=str, part_description=str, quantity_purchased=int, price=Decimal('0.00')):
        """Initializer for invoice class that takes part number, part description, quantity purcashed and price of object."""
        self.part_number = part_number
        self.part_description = part_description
        self.quantity_purchased = quantity_purchased
        self.part_price = price    
    

    @property
    def part_number(self):
        """Returns the part number"""
        return self._part_number


    @part_number.setter
    def part_number(self, number):
        """Sets the part number."""
        self._part_number = number


    @property
    def part_description(self):
        """Returns the part description."""
        return self._part_description


    @part_description.setter
    def part_description(self, description):
        """Sets the part description"""
        self._part_description = description


    @property
    def quantity_purchased(self):
        """Returns the quantity purchased."""
        return self._quantity_purchased


    @quantity_purchased.setter
    def quantity_purchased(self, quantity):
        """Sets the quantity purchased."""
        if quantity < 0:
            raise ValueError('Quantity must be greater than 0.')

        self._quantity_purchased = quantity

    
    @property
    def part_price(self):
        """Returns the price of the part."""
        return self._part_price


    @part_price.setter
    def part_price(self, price):
        """Sets the price of the part."""
        if price < Decimal('0.00'):
            raise ValueError('Quantity must be greater than 0.')

        self._part_price = price


    def calculate_invoice(self):
        return (self.quantity_purchased * self.part_price)


    def __str__(self):
        return (f'Part Number: {self.part_number}\n' +
            f'Part Description: {self.part_description}\n' +
            f'Quantity Purchased: {self.quantity_purchased}\n' + 
            f'Price of Part: {self.part_price}')