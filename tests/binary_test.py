from unittest import TestCase
import random
from binary import Binary

class BinaryConversionInteger(TestCase):
    """
    Test conversion of integer to binary is correct
    """
    def test_valid_conversion_of_integer_number(self):
        self.assertEqual(Binary.convert(12343), '11000000110111')

class BinaryConversionFractional(TestCase):
    """
    Test conversion of fractional number to binary is correct
    """
    def test_valid_conversion_of_fractional_number(self):
        self.assertEqual(Binary.convert_fractional(0.17), '00101')


if __name__ == '__main__':
    unittest.main()