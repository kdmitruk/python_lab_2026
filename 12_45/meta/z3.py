class Register(type):
    register = {}

    def __new__(cls,name,base,fields):
        result = super().__new__(cls,name,base,fields)
        Register.register[name] = result
        return result

class Test1(metaclass = Register):
    def __init__(self,pole):
        self.pole = pole

class Test2(metaclass = Register):
    def __init__(self):
        pass

if __name__ == '__main__':
     test1 = Test1("cad")
     print(Register.register)