from fraction import Fraction
from mixedfraction import MixedFraction


def main():
    half = Fraction(3,9)
    print(half.is_integer())
    print(half)
    print(float(half))
    f = Fraction(1, 2)
    print(5 * half)
    try:
        print(half/f)
    except ZeroDivisionError:
        print("Źle ")
    print(half + f)
    print(half - f)

    f2 = MixedFraction(4,3)
    print(f2 * 2)

if __name__ == '__main__':
    main()