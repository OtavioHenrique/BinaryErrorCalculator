class Binary:
    """
    This class is a representation of a binary number

    Args:
         _number (:obj:`list` of str):
             List representing the integer part of binary number.
         _decimal (:obj:`list` of str):
             List representing the decimal part of binary number.
    """
    def __init__(self, *, number, decimal):
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

    def as_decimal(self):
        """Returns the decimal representation of self (Binary)"""
        converted_decimal_part = self._decimal_as_decimal()
        converted_integer_part = self._integer_as_decimal()

        return converted_decimal_part + converted_integer_part

    def __add__(self, number):
        """
        Sum two binary numbers

        Args:
            number: The number to be add (As binary instance)

        Returns:
            The final binary resulting by the sum
        """
        return self._sum(number)

    def _sum(self, number):
        bigger_number, lower_number = self._normalize(number._decimal)

        final_number = []

        bigger_number = bigger_number[::-1]
        lower_number = lower_number[::-1]

        rest = 0

        for index, _ in enumerate(bigger_number):
            binary_sum = lower_number[index] + bigger_number[index] + rest

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

        return Binary(number=[0], decimal=final_number[::-1])

    def _normalize(self, number):
        if len(self._decimal) > len(number):
            lower_number = number
            bigger_number = self._decimal
        else:
            lower_number = self._decimal
            bigger_number = number

        for _ in range(len(bigger_number) - len(lower_number)):
            lower_number.insert(0, 0)

        return (bigger_number, lower_number)

    def _integer_as_decimal(self):
        final_number = 0
        for position, number in enumerate(self._number[::-1]):
            final_number += number * pow(2, position)

        return final_number

    def _decimal_as_decimal(self):
        final_number = 0

        for position, number in enumerate(self._decimal, 1):
            final_number += number * pow(2, -position)

        return final_number
