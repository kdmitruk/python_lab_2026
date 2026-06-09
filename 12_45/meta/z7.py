from time import time

is_debug = False

def debug(f):
    def wrapper(*args, **kwargs):
        global is_debug
        is_debug = True
        result = f(*args, **kwargs)
        is_debug = False
        return result
    return wrapper

def printd(*args, **kwargs):
    if is_debug:
        print(*args, **kwargs)

@debug
def hello_world():
    print("cokolwiek")
    printd("cos d")

if __name__ == '__main__':
    hello_world()