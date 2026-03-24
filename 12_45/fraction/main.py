from fraction import Fraction

def main():
    half = Fraction(3,7)
    print(half.is_integer())
    print(half)
    print(float(half))

if __name__ == '__main__':
    main()