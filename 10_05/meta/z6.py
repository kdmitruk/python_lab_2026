from time import time

def log(function):
    def wrapper(*args, **kwargs):
        stime = time()
        result = function(*args, **kwargs)
        endtime = time() - stime
        print("Trwalo ", endtime)
        return result
    return wrapper
@log
def printHelloWorld():
    for i in range(1000000000):
        pass

if __name__ == '__main__':
    printHelloWorld()
