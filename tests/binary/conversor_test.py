from unittest import TestCase
from binary_error_calculator.binary.conversor import Conversor

class BinaryConversionInteger(TestCase):
    """
    Test conversion of integer to binary is correct
    """
    def test_valid_conversion_of_integer_number(self):
        conversor = Conversor(number=12343)

        self.assertEqual(conversor.convert_integer(), '11000000110111')

class BinaryConversionDecimal(TestCase):
    """
    Test conversion of decimal number to binary is correct
    """
    def test_valid_conversion_of_decimal_number(self):
        conversor = Conversor(number=0.17, precision=5)

        self.assertEqual(conversor.convert_decimal(), '00101')

class BinaryConversion(TestCase):
    """
    Test conversion of number to binary (Returning a instance of Binary)
    """
    def test_valid_conversion_of_number_to_binary(self):
        conversor = Conversor(number=12343.17, precision=5)
        binary = conversor.convert()

        self.assertEqual(binary.number(), '11000000110111')
        self.assertEqual(binary.decimal(), '00101')
