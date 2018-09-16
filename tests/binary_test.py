from unittest import TestCase
from binary_error_calculator.binary import Binary


class SumTest(TestCase):
    """Test the sum between two binary numbers"""
    def test_valid_sum(self):
        binary = Binary(number=[0], decimal=[0, 0, 1, 0, 1])
        binary2 = Binary(number=[0], decimal=[1])

        binary_result = binary + binary2

        self.assertEqual(binary_result.decimal, '00110')


class AsDecimalTest(TestCase):
    """Test if it is converting binary to decimal correctly"""
    def test_valid_conversion(self):
        binary = Binary(number=[1, 0, 1], decimal=[1, 1, 0])

        self.assertEqual(binary.as_decimal(), 5.75)


if __name__ == '__main__':
    unittest.main()
