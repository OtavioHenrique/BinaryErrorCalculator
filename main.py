class Binary:
    def __init__(self, number, decimal):
        self.number = number
        self.decimal = decimal

    @classmethod
    def convert(self, number):
        remainder = None
        binary = []
        result = number

        while result != 0:
            remainder = result % 2
            result = result // 2
            binary.append(remainder)


        aux = ''.join(str(x) for x in binary)
        return aux[::-1]

    @classmethod
    def convert_decimal(self, number, precision=6):
        decimal = round(number % 1, precision)

        binary = []

        for x in range(precision):
            aux = decimal * 2
            if aux > 1:
              binary.append(1)
              decimal = round(aux % 1, precision)
              continue

            binary.append(0)
            decimal = aux

        return ''.join(str(x) for x in binary)

# print(Binary.convert(48))
# print(Binary.convert_decimal(48.45))
# print(",".join(convert_binary(17)))
