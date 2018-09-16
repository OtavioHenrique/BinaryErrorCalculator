from unittest import TestCase
from binary_error_calculator.experimental_error_calculator \
    import ExperimentalErrorCalculator


class ExperimentalErrorCalculatorTest(TestCase):
    def test_correct_calculus(self):
        known_value = 0.17
        experimental_value = 0.1875
        experimental_calculator = ExperimentalErrorCalculator(
            known_value=known_value,
            experimental_value=experimental_value
        )

        self.assertEqual(
            experimental_calculator.calculate(),
            10.294117647058815
        )
