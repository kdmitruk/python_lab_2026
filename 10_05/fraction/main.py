from fraction import Fraction


def main():
    fraction = Fraction(3, 4)
    print(f"{fraction.numerator}, {fraction.denominator}")
    print(fraction.is_integer())
    fraction2 = Fraction(4, 2)
    print(fraction2.is_integer())
    print(fraction2.__str__())
    print(fraction2)
    print(fraction2.__float__())
    print(float(fraction2))
    fraction3=Fraction(2,6)
    print(fraction*fraction3)
    print(fraction*2)
    print(3*fraction)
    try:
        print(fraction/Fraction(0,5))
    except ZeroDivisionError:
        print("ŹLE!")



if __name__ == '__main__':
    main()