import numpy as np

def zadanie1():

    arr=np.array([255,20,30,40],dtype=np.uint8)
    print(arr)
    arr2=np.array([[10,20,30],[40,50,60]])
    print(arr2)
    print(arr2.shape)
    print(arr2.dtype)
if __name__ == '__main__':
    zadanie1()