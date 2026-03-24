class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def is_integer(self):
        return self.numerator % self.denominator == 0