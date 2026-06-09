class VerboseValue:
    def __init__(self, value):
        self.value= value
        print("Poczatkowa wartosc: ", self.value)

    def __get__(self, instance, owner):
        print("Odczytano wartosc")
        return self.value

    def __set__(self, instance, value):
        print("Ustawiono wartosc")
        return self.value

class Test:
    value = VerboseValue(0)
    def __init__(self, value):
        Test.value = VerboseValue(value)

if __name__ == '__main__':
    test = Test("test")
    print(test.value)
    Test.value="asdasd"
    print(test.value)