class ExperimentalErrorCalculator():
    def __init__(self, known_value, experimental_value):
        self.known_value = known_value
        self.experimental_value = experimental_value

    def calculate(self):
        return (abs(self.experimental_value - self.known_value) / self.known_value) * 100
