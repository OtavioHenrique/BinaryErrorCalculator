from unittest import TestCase
import random
from binary import Binary

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

        self.assertEqual(binary.max_approximation(), '00110')

if __name__ == '__main__':
    unittest.main()
