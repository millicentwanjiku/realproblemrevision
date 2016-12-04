"""implements inheritance"""
from drinks import Drinks

class Beverages(Drinks):
    """Beverages inherits from class Drink"""
    __type = 'coffee'

    def _init_(self):
        """Extension of the drinks constructor"""
        super(Drinks, self)._init_()
        self.__type = "coffee"

    def set_type(self, types):
        """Sets type"""
        self.__type = types

class Softdrinks(Drinks):
    """Beverages inherits from class Drink"""
    __type = 'coke'

    def _init_(self):
        """Extension of drinks constructor"""
        super(Drinks, self)._init_()
        self.__type = "coke"

    def set_type(self, types):
        """sets type"""
        self.__type = types
