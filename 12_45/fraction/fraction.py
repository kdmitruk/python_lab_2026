import math


class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ZeroDivisionError
        self.numerator = numerator
        self.denominator = denominator
        self.__reduce()

    def is_integer(self):
        return self.numerator % self.denominator == 0

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    def __float__(self):
        return self.numerator/self.denominator

    def __reduce(self):
        divisor = math.gcd(self.denominator,self.numerator)
        self.numerator//=divisor
        self.denominator//=divisor

    def __rmul__(self, other):
        return self * other

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(
                self.numerator * other.numerator,
                self.denominator * other.denominator
            )
        elif isinstance(other, int):
            return Fraction(
                self.numerator * other,
                self.denominator
            )
        else:
            return NotImplemented

    def __truediv__(self, other):
        return Fraction(
            self.numerator * other.denominator,
            self.denominator * other.numerator
        )

    def __add__(self, other):
        return self.common_add_sub(other, lambda a, b:a+b)

    def __sub__(self, other):
        return self.common_add_sub(other, lambda a, b:a-b)

    def common_add_sub(self, other, operation):
        return Fraction(
            operation(self.numerator*other.denominator,other.numerator*self.denominator),
            self.denominator*other.denominator
        )