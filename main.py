from binary_error_calculator.conversor import Conversor
from binary_error_calculator.max_approximation import MaxApproximation
from binary_error_calculator.experimental_error_calculator import ExperimentalErrorCalculator

number = float(input("Please, enter with a number in the interval ]0,1[: "))
while( number <= 0 or number >= 1):
    number = float(input("Please, enter with a number in the interval ]0,1[: "))

for precision in range(5, 12+1):

    binary = Conversor(number=number, precision=precision).convert()

    max_approximation = MaxApproximation.calculate(binary)
    error_percent = ExperimentalErrorCalculator(
                        known_value = number,
                        experimental_value = max_approximation.as_decimal()
                    ).calculate()

    print('--------------------------------------------')
    print(f"Calculating for {precision} decimal places of precision.")
    print(f"Minimum Approximation {binary.as_decimal()}")
    print(f"Maximum Approximation {max_approximation.as_decimal()}")
    print(f"Error Percentage: {str(error_percent)}")
    print('--------------------------------------------')
