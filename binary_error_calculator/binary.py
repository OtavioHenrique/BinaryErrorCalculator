class Binary:
    """This class is a representation of a binary number

    Args:
        _number (:obj:`list` of str): List representing the integer part of binary number
        _decimal (:obj:`list` of str): List representing the decimal part of binary number.
    """
    def __init__(self, number, decimal=[0]):
        self._number = number
        self._decimal = decimal

    @property
    def number(self):
        """str: Represents integer part of binary number as string."""
        return ''.join(str(x) for x in self._number)

    @property
    def decimal(self):
        """str: Represents decimal part of binary number as string."""
        return ''.join(str(x) for x in self._decimal)

    def max_approximation(self):
        """Returns the max approximation of a binary number (number + 1)"""
        return self + Binary([0],[1])

    def __add__(self, number):
        """
        Sum two binary numbers

        Args:
            number: The number to be add

        Returns:
            The final binary resulting by the sum
        """
        number = self._normalize(self._decimal, [number._decimal])
        final_number = []
        decimal_number = self._decimal[::-1]
        number = number[::-1]

        rest = 0

        for index in range(len(decimal_number)):
            sum = number[index] + decimal_number[index] + rest

            if sum == 0:
                final_number.append(0)
                rest = 0
            elif sum == 1:
                final_number.append(1)
                rest = 0
            elif sum == 2:
                final_number.append(0)
                rest = 1
            elif sum == 3:
                final_number.append(1)
                rest = 1

        return Binary([0], final_number[::-1])

    @classmethod
    def convert(cls, number):
        """
        Convert number to binary

        Args:
            number: Integer number to be converted

        Returns:
            A instance of binary class with binary number
        """
        remainder = None
        binary = []
        result = int(number)

        while result != 0:
            remainder = result % 2
            result = result // 2
            binary.append(remainder)

        return Binary(binary[::-1])

    @classmethod
    def convert_fractional(cls, number, precision=5):
        """
        Convert a number with decimal part to binary

        Args:
            number: Number to be converted

        Returns:
            A instance of binary class with binary number
        """
        decimal = round(number % 1, precision)

        binary = []

        for _ in range(precision):
            aux = decimal * 2
            if aux > 1:
                binary.append(1)
                decimal = round(aux % 1, precision)
                continue

            binary.append(0)
            decimal = aux

        return Binary(number, binary)

    def _normalize(self, number1, number2):
        final_number = number2[0]
        for _ in range(len(number1) - len(number2)):
            final_number.insert(0, 0)

        return final_number
