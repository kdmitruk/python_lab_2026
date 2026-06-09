def log(function):
    def wrapper(*args, **kwargs):
        print(f"Rozpoczeto {function.__name__}")
        result = function(*args, **kwargs)
        print(f"Zakonczono {function.__name__}")
        return result
    return wrapper
@log
def printHelloWorld():
    print("Hello World!")

if __name__ == '__main__':
    printHelloWorld()