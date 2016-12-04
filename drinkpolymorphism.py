"""implementation of polymorphism"""
import unittest
from drinkinstant import get_contents

class Tester(unittest.TestCase):
    """Tests classes Softdrinks and Beverages"""

    def Teststring(self):
        """Tests if get contents will return a string"""
        new_softdrink = Softdrinks()
        new_softdrink.set_type('coke')
        self.assertEqual(get_contents(new_softdrink),
                         ['yellow', 5222, 'pink', 250, 'coke'])

    def Testint(self):
        """Tests if get contents will return an integer"""
        new_beverage = Beverages()
        new_beverage.set_stock(10)
        self.assertEqual(get_contents(new_beverage),
                         ['yellow', 5222, 'brown', 250, 10])
