import unittest
from src.calculator import add, divide, multiply, subtract

class TestCalculator(unittest.TestCase):

# 1. Arrange
# 2. Act
# 3. Assert

    def test_add(self):
        actual = add(2, 3)
        self.assertEquals(5, actual)

    def test_subtract(self):
        self.assertEquals(3, subtract(10, 7))

pass