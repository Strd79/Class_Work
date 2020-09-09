import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Homer", 100)

    def test_customer_name(self):
        customer_name = self.customer.name
        self.assertEqual("Homer", customer_name)

    def test_customer_wallet(self):
        customer_wallet = self.customer.wallet
        self.assertEqual(100, customer_wallet)

    def test_remove_from_customer_wallet(self):
        self.customer.remove_from_customer_wallet(20)
        self.assertEqual(80, self.customer.wallet)