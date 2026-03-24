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

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ZeroDivisionError
        return Fraction(
            self.numerator*other.denominator,
            self.denominator*other.numerator
        )

    def __add__(self, other):
        return self.__common(other, lambda a, b: a+b)

    def __sub__(self,other):
        return self.__common(other, lambda a, b: a-b)

    def __common(self, other, operation):
        if self.denominator == other.denominator:
            return Fraction(operation (self.numerator, other.numerator), self.denominator)
        else:
            return Fraction(self.numerator*other.denominator+other.numerator*self.denominator,
                            self.denominator*other.denominator)