from .binary import Binary

class Conversor:
    def __init__(self, *, number, precision=5):
        self.number = number
        self.precision = precision

    def convert(self):
        integer = self._integer_to_binary()
        decimal = self._decimal_to_binary()

        return Binary(number=integer, decimal=decimal)

    def convert_integer(self):
        """
        Converts integer part of number to binary

        Returns:
            A string with integer part of number as binary number
        """
        binary = self._integer_to_binary()
        return self._convert_to_string(binary)

    def convert_decimal(self):
        """
        Converts decimal part of number to binary

        Returns:
            A string with decimal of number part as binary number
        """
        binary = self._decimal_to_binary()
        return self._convert_to_string(binary)

    def _convert_to_string(self, array):
        return ''.join(str(number) for number in array)

    def _decimal(self):
        return round(self.number % 1, self.precision)

    def _integer(self):
        return int(self.number)

    def _integer_to_binary(self):
        remainder = None
        binary = []
        result = self._integer()

        while result != 0:
            remainder = result % 2
            result = result // 2
            binary.append(remainder)

        return binary[::-1]

    def _decimal_to_binary(self):
        decimal = self._decimal()

        binary = []

        for _ in range(self.precision):
            aux = decimal * 2
            if aux > 1:
                binary.append(1)
                decimal = round(aux % 1, self.precision)
                continue

            binary.append(0)
            decimal = aux

        return binary
