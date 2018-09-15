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
        return self + Binary([0], [1])

    def as_decimal(self):
        """Returns the decimal representation of self (Binary)"""
        converted_decimal_part = self._decimal_as_decimal()
        converted_integer_part = self._integer_as_decimal()

        return converted_decimal_part + converted_integer_part

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

        for index, _ in enumerate(decimal_number):
            binary_sum = number[index] + decimal_number[index] + rest

            if binary_sum == 0:
                final_number.append(0)
                rest = 0
            elif binary_sum == 1:
                final_number.append(1)
                rest = 0
            elif binary_sum == 2:
                final_number.append(0)
                rest = 1
            elif binary_sum == 3:
                final_number.append(1)
                rest = 1

        return Binary([0], final_number[::-1])

    @classmethod
    def convert(cls, number, *, precision=5):
        decimal = cls.__extract_decimal(number)
        integer = cls.__extract_integer(number)

    def __convert_integer(cls, number):
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

    def __convert_fractional(cls, number, precision=5):
        """
        Convert a number with decimal part to binary

        Args:
            number: Number to be converted

        Returns:
            A instance of binary class with binary number
        """
        decimal = self.__extract_decimal(number)

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

    def __extract_decimal(self, number, *, precision=5):
        return round(number % 1, precision)

    def __extract_integer(self, number, *, precision=5):
        return int(number)

    def _normalize(self, number1, number2): #This is not working at all cases, must compare two numbers before normalize
        final_number = number2[0]
        for _ in range(len(number1) - len(number2)):
            final_number.insert(0, 0)

        return final_number

    def _integer_as_decimal(self): #maybe private methods should start with __
        final_number = 0
        for position, number in enumerate(self._number[::-1]):
            final_number += number * pow(2, position)

        return final_number

    def _decimal_as_decimal(self):
        final_number = 0

        for position, number in enumerate(self._decimal, 1):
            final_number += number * pow(2, -position)

        return final_number
