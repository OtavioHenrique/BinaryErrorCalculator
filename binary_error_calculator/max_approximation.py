from binary_error_calculator.conversor import Conversor
from binary_error_calculator.binary import Binary

class MaxApproximation:
    @classmethod
    def calculate(cls, number):
        """Returns the max approximation of a binary number (number + 1)"""
        return number + Binary(number=[0], decimal=[1])
