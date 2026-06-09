from argparse import ArgumentError


class ForceArguments(type):
    allowed_fields=["firstname", "lastname", "email"]

    def __new__(cls,name,base,fields):
        result = super().__new__(cls,name,base,fields)
        for name in ForceArguments.allowed_fields:
            if name not in fields:
                raise ArgumentError(None,f"Klucza {name} nie ma na liscie argumentow")
        return result

class Test1(metaclass= ForceArguments):
    firstname = None
    def __init__(self,pole):
        self.firstname = pole

if __name__ == '__main__':
    test = Test1("asdasda")