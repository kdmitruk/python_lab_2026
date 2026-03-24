from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.__reduce()
    def __reduce(self):
        nwd = gcd(self.numerator, self.denominator)
        self.numerator //= nwd
        self.denominator //= nwd

    def is_integer(self):
        return self.numerator % self.denominator == 0

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __float__(self):
        return self.numerator/self.denominator


