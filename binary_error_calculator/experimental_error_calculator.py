class ExperimentalErrorCalculator:
    """
    This class calculate the experimental error between two numbers.

    Args:
         _experimental_value (:obj:`decimal/integer`):
             Known value to be used at calculus.
         _experimental_value (:obj:`decimal/integer`):
             Value obtained during experiment.
    """
    def __init__(self, known_value, experimental_value):
        self.known_value = known_value
        self.experimental_value = experimental_value

    def calculate(self):
        """Calculate the experimental error"""
        return (abs(self._difference()) / self.known_value) * 100

    def _difference(self):
        return self.experimental_value - self.known_value
