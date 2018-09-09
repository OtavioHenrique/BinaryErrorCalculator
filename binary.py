class Binary:
    def __init__(self, number, decimal):
        self._number = number
        self._decimal = decimal

    @property
    def number(self):
        binary = ''.join(str(x) for x in self._number)
        return binary

    @property
    def decimal(self):
        final_decimal = ''.join(str(x) for x in self._decimal)
        return final_decimal

    @classmethod
    def convert(cls, number):
        remainder = None
        binary = []
        result = int(number)

        while result != 0:
            remainder = result % 2
            result = result // 2
            binary.append(remainder)

        return Binary(binary[::-1], [0])

    @classmethod
    def convert_fractional(cls, number, precision=5):
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
