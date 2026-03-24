from fraction import Fraction
class MixedFraction(Fraction):
    def __str__(self):
        whole = self.numerator // self.denominator
        numerator_rest = self.numerator % self.denominator
        if numerator_rest == 0:
            return str(whole)
        elif whole == 0:
            return super().__str__()
        else:
            return f"{whole} {numerator_rest}/{self.denominator}"

    # 4/3 --> 1 1/3