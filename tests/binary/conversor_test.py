from unittest import TestCase
from binary_error_calculator.binary.conversor import conversor

class BinaryConversionInteger(TestCase):
    """
    Test conversion of integer to binary is correct
    """
    def test_valid_conversion_of_integer_number(self):
        binary = Binary.convert(12343)

        self.assertEqual(binary.number, '11000000110111')

class BinaryConversionFractional(TestCase):
    """
    Test conversion of fractional number to binary is correct
    """
    def test_valid_conversion_of_fractional_number(self):
        binary = Binary.convert_fractional(0.17)

        self.assertEqual(binary.decimal, '00101')


