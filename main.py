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

        return ''.join(str(x) for x in binary)

    @classmethod
    def convert_decimal(self, number, precision=2):
        decimal = round(number % 1, precision)

        return decimal

print(Binary.convert_decimal(17.14))
# print(",".join(convert_binary(17)))
