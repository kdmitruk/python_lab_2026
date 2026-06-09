class VerboseValue:
    def __init__(self,value):
        self.value = value
        print(f"Zainicjalizowano wartość: {value}")

    def __get__(self, instance, owner):
        print(f"Odczytujemy wartość która jest równa : {self.value}")
        return self.value

    def __set__(self, instance, value):
        self.value = value
        print(f"Ustawiamy wartość która jest równa : {self.value}")


class Y:
    x = VerboseValue(5)

if __name__ == '__main__':
    y=Y()
    y.x = "Ala ma kota"
    print(Y.x)