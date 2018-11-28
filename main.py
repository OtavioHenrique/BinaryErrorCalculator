from binary_error_calculator.conversor import Conversor
from binary_error_calculator.max_approximation import MaxApproximation
from binary_error_calculator.experimental_error_calculator import ExperimentalErrorCalculator

number = float(input("Please, enter with a number in the interval ]0,1[: "))
while( number <= 0 or number >= 1):
    number = float(input("Please, enter with a number in the interval ]0,1[: "))

for precision in range(5, 12+1):
    binary = Conversor(number=number, precision=precision).convert()
    error_percent_min_apprx = ExperimentalErrorCalculator(
                                  known_value = number,
                                  experimental_value = binary.as_decimal()
                              ).calculate()

    max_approximation = MaxApproximation.calculate(binary)
    error_percent_max_apprx = ExperimentalErrorCalculator(
                                  known_value = number,
                                  experimental_value = max_approximation.as_decimal()
                              ).calculate()

    print("Calculating for " + str(precision) + "decimal places of precision.")
    print("Minimum Approximation as decimal " + str(binary.as_decimal()))
    print("Minimum Approximation as binary " + str(binary))
    print("Error Percentage for minimum approximation: " + str(error_percent_min_apprx) + "%")
    print("Maximum Approximation " + str(max_approximation.as_decimal()))
    print("Maximum Approximation as binary " + str(max_approximation))
    print("Error Percentage for maximum approximation: " + str(error_percent_max_apprx) + "%")
    print('--------------------------------------------')
