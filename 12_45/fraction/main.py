from fraction import Fraction

def main():
    half = Fraction(3,9)
    print(half.is_integer())
    print(half)
    print(float(half))
    f = Fraction(4, 2)
    print(5 * half)

if __name__ == '__main__':
    main()