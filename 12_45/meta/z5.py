def log(f):
    def wrapper(*args, **kwargs):
        print("Zaczęto wywoływać funkcję", f.__name__)
        result = f(*args, **kwargs)
        print("Zakończono wywoływać funkcję", f.__name__)
        return result
    return wrapper

@log
def hello_world():
    print("Hello world")

if __name__ == '__main__':
    hello_world()