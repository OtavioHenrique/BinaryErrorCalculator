from unittest import TestCase
from binary_error_calculator.binary.conversor import Conversor

class BinaryConversionInteger(TestCase):
    """
    Test conversion of integer to binary is correct
    """
    def test_valid_conversion_of_integer_number(self):
        conversor = Conversor(number=12343)
        self.assertEqual(conversor.convert_integer(), '11000000110111')

class BinaryConversionFractional(TestCase):
    """
    Test conversion of fractional number to binary is correct
    """
    def test_valid_conversion_of_fractional_number(self):
        conversor = Conversor(number=0.17, precision=5)
        self.assertEqual(conversor.convert_decimal(), '00101')

