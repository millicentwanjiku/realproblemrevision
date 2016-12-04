"""implements inheritance"""
from drinks import Drinks

class Beverages(Drinks):
    """Beverages inherits from class Drink"""
    stock = 10

    def _init_(self):
        """Extension of the drinks constructor"""
        super(Drinks, self)._init_()
        self.type = "coffee"

    def set_type(self, types):
        """Sets type"""
        self.type = stock

    def get_type(self):
        """Gets stock"""
        return self.stock

class Softdrinks(Drinks):
    """Beverages inherits from class Drink"""
    type = 'coke'

    def _init_(self):
        """Extension of drinks constructor"""
        super(Drinks, self)._init_()
        self.type = "coke"

    def set_type(self, types):
        """sets type"""
        self.type = types

    def get_type(self):
        """Gets type"""
        return self.type
