"""Real world oop problem"""

class Drinks():
    """Implementation of class drinks"""

    colour = ''
    price = 0
    ingredient = ''
    quantity = 0

    def __init__(self, colours, prices, ingredients, quantity):
        """This is the constructor"""

        self.colour = colours
        self.price = prices
        self.ingredient = ingredients
        self.quantit = quantity

        def set_colour(self, colours):
            """Sets colour"""
            self.colour = colours

        def set_price(self, prices):
            """Sets prices"""
            self.price = prices

        def set_ingredient(self, ingredients):
            """Sets ingredients"""
            self.ingredient = ingredients

        def set_quantit(self, quantity):
            """Sets quantity"""
            self.quantit = quantity
