from time import time

def log(f):
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        print(f"Trwalo {time() - start}")
        return result
    return wrapper

@log
def hello_world():
    for _ in range(1,1000000000):
        pass

if __name__ == '__main__':
    hello_world()