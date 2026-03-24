from fraction import Fraction

def main():
    fraction = Fraction(3, 4)
    print(f"{fraction.numerator}, {fraction.denominator}")
    print(fraction.is_integer())
    fraction2 = Fraction(4, 2)
    print(fraction2.is_integer())

if __name__ == '__main__':
    main()