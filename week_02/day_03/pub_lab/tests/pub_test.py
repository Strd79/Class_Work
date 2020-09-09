import unittest
from src.pub import Pub 

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)

    def test_pub_has_name(self):
        pub_name = self.pub.name
        self.assertEqual("The Prancing Pony", pub_name)

    def test_till_amount(self):
        till_amount = self.pub.till
        self.assertEqual(100, till_amount)

    def test_increase_till_amount(self):
        self.pub.increase_till_amount(50)
        self.assertEqual(150, self.pub.till)
