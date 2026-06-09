import inspect


class ForceArguments(type):
    __allowed_fields = ["email", "first_name"]

    def __new__(cls,name,base,fields):
        result = super().__new__(cls,name,base,fields)
        # for argument in ForceArguments.__allowed_fields :
        #     if argument not in fields:
        #         raise   Exception(f"{argument} nie znajduje się na liście force")
        init=fields['__init__']
        print(inspect.signature(init))
        return result

class Test1(metaclass = ForceArguments):
    email = None
    def __init__(self,email,password):
        self.email = email
if __name__ == '__main__':
     test1 = Test1("cad","haslo")