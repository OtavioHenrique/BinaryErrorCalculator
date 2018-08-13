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


print(Binary.convert(17))
# print(",".join(convert_binary(17)))
