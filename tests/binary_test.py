from unittest import TestCase
import random
from binary_error_calculator.binary import Binary

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

class MaxApproximation(TestCase):
    """
    Test if it's return the right max approximation of the binary number
    """
    def test_valid_max_approximation(self):
        binary = Binary([0], [0, 0, 1, 0, 1])
        max_approximation = binary.max_approximation()

        self.assertEqual(max_approximation.decimal, '00110')

class Sum(TestCase):
    """
    Test the sum between two binary numbers
    """
    def test_valid_sum(self):
        binary = Binary([0], [0, 0, 1, 0, 1])
        binary2 = Binary([0], [1])

        binary_result = binary + binary2

        self.assertEqual(binary_result.decimal, '00110')


if __name__ == '__main__':
    unittest.main()
