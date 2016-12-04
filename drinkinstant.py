"""Implementation of the instance method"""
from drinks import Drinks
from drinksinheritance import Softdrinks
from drinksinheritance import Beverages

def get_contents(objects):
    """Gets objects from their respective classes"""
    contents = []
    contents.append(objects.ingredient)
    contents.append(objects.quantit)
    contents.append(objects.colour)
    contents.append(objects.price)
    contents.append(objects.get_type())
    return contents

x=Softdrinks('pink',250,'yellow',5222)
print get_contents(x)
y=Beverages('brown',250,'yellow',5222)
print get_contents(y)