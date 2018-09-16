from unittest import TestCase
from binary_error_calculator.binary import Binary
from binary_error_calculator.max_approximation import MaxApproximation


class MaxApproximationTest(TestCase):
    """
    Test if it's return the right max approximation of the binary number
    """
    def test_valid_max_approximation(self):
        binary = Binary(number=[0], decimal=[0, 0, 1, 0, 1])
        max_approximation = MaxApproximation.calculate(binary)

        self.assertEqual(max_approximation.decimal, '00110')
