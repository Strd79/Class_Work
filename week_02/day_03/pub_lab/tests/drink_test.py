import unittest
from src.drink import Drink
from src.pub import Pub

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink_1 = Drink("Duff Beer", 10.50)
        self.drink_2 = Drink("Springfield Slammer", 15)
        self.drink_3 = Drink("Diet Coke", 5)

        self.pub = Pub("The Prancing Pony", 100.00)
    
    def test_add_drink(self):
        self.pub.add_drink(self.pub, self.drink_1)
        self.assertEqual(1, len(self.pub.drinks))