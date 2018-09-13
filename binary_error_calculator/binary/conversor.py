class Conversor:
    def __init__(self, number):
        self.number = number

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

