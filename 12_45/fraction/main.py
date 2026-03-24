from fraction import Fraction

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

if __name__ == '__main__':
    main()