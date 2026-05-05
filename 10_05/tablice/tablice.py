import numpy as np
import matplotlib.pyplot as plt

def zadanie1():
    arr=np.array([255,20,30,40],dtype=np.uint8)
    print(arr)
    arr2=np.array([[10,20,30],[40,50,60]])
    print(arr2)
    print(arr2.shape)
    print(arr2.dtype)

def zadanie2():
    arr=np.zeros((100,100), dtype = np.uint8)
    arr[40,60]=255
    plt.imshow(arr, cmap="gray")
    plt.show()

def zadanie3():
    arr = np.random.randint(0, 256, (100,100), dtype=np.uint8)
    plt.imshow(arr, cmap="gray")
    plt.show()

if __name__ == '__main__':
    zadanie3()