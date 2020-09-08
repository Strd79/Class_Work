import unittest

from classes.pet_shop import PetShop
from classes.pet import Pet
from classes.customer import Customer

class TestPetShop(unittest.TestCase):
    def setUp(self):
        self.pet_1 =  Pet("Sir Percy", "cat", "British Shorthair", 500)
        self.pet_2 =  Pet("King Arthur", "dog", "Husky", 900)

        pets = [self.pet_1, self.pet_2]
        self.pet_shop = PetShop("Camelot of Pets", pets, 1000)

    def test_pet_shop_has_name(self):
        self.assertEqual("Camelot of Pets", self.pet_shop.name)

    # @unittest.skip("delete this line to run the test")
    def test_pet_shop_case(self):
        self.assertEqual(1000, self.pet_shop.total_cash)

    # @unittest.skip("delete this line to run the test")
    def test_pet_shop_pets_sold_starts_at_0(self):
        self.assertEqual(0, self.pet_shop.pets_sold)

    # @unittest.skip("delete this line to run the test")
    def test_pet_shop_stock_count(self):
        self.assertEqual(2, self.pet_shop.stock_count())

    # @unittest.skip("delete this line to run the test")
    def test_increase_pets_sold(self):
        self.pet_shop.increase_pets_sold()
        self.assertEqual(1, self.pet_shop.pets_sold)

    # @unittest.skip("delete this line to run the test")
    def test_can_increase_total_cash(self):
        self.pet_shop.increase_total_cash(500)
        self.assertEqual(1500, self.pet_shop.total_cash)

    # @unittest.skip("delete this line to run the test")
    def test_can_add_pet_to_stock(self):
        new_pet = Pet("Lancelot", "dog", "Basset Hound", 750)
        self.pet_shop.add_pet(new_pet)
        self.assertEqual(3, self.pet_shop.stock_count())

    # @unittest.skip("delete this line to run the test")
    def test_can_remove_pet_from_stock(self):
        self.pet_shop.remove_pet(self.pet_1)
        self.assertEqual(1, self.pet_shop.stock_count())

    # @unittest.skip("delete this line to run the test")
    def test_can_find_pet_by_name(self):
        pet = self.pet_shop.find_pet_by_name("Sir Percy")
        self.assertEqual("Sir Percy", pet.name)

    # @unittest.skip("delete this line to run the test")
    def test_can_sell_pet_to_customer(self):
        customer = Customer("Jack Jarvis", 1000)
        self.pet_shop.sell_pet_to_customer("Sir Percy", customer)
        self.assertEqual(1, customer.pet_count())
        self.assertEqual(1, self.pet_shop.stock_count())
        self.assertEqual(1, self.pet_shop.pets_sold)
        self.assertEqual(1500, self.pet_shop.total_cash)
