from math import gcd

from sympy.physics.optics import FreeSpace


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

    def __rmul__(self, other):
        return self*other

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(
                self.numerator*other.numerator,
                self.denominator*other.denominator
            )
        elif isinstance(other,int):
            return Fraction(
                self.numerator*other,
                self.denominator
            )


        else:
            return NotImplemented
