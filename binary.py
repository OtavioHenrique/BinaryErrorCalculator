class Binary:
    def __init__(self, number, decimal = [0]):
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

    def max_approximation(self):
        number = self.add(self.__normalize(self._decimal, [1]))
        return ''.join(str(x) for x in number)

    def add(self, number):
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

        return final_number[::-1]

    @classmethod
    def convert(cls, number):
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
        decimal = round(number % 1, precision)

        binary = []

        for _ in range(precision): #TODO: use enumerate() https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops
            aux = decimal * 2
            if aux > 1:
                binary.append(1)
                decimal = round(aux % 1, precision)
                continue

            binary.append(0)
            decimal = aux

        return Binary(number, binary)

    def __normalize(self, number1, number2): #TODO: It's need to be something like Binary.normalize(number)
        for number in range(len(number1) - len(number2)):
            number2.insert(0, 0)

        return number2
