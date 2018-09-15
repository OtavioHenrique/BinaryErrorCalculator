from unittest import TestCase
import random
from binary_error_calculator.binary import Binary

class MaxApproximation(TestCase):
    """
    Test if it's return the right max approximation of the binary number
    """
    def test_valid_max_approximation(self):
        binary = Binary([0], [0, 0, 1, 0, 1])
        max_approximation = binary.max_approximation()

        self.assertEqual(max_approximation.decimal, '00110')

class Sum(TestCase):
    """Test the sum between two binary numbers"""
    def test_valid_sum(self):
        binary = Binary([0], [0, 0, 1, 0, 1])
        binary2 = Binary([0], [1])

        binary_result = binary + binary2

        self.assertEqual(binary_result.decimal, '00110')

class AsDecimalTest(TestCase):
    """Test if it is converting binary to decimal correctly"""
    def test_valid_conversion(self):
        binary = Binary([1, 0, 1], [1, 1, 0])

        self.assertEqual(binary.as_decimal(), 5.75)

if __name__ == '__main__':
    unittest.main()
