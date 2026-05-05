import math
from pickletools import uint8

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
    return arr
    # plt.imshow(arr, cmap="gray")
    # plt.show()

def zadanie4():
    arr = np.random.normal(128, 25, (100,100))
    return arr
    # plt.imshow(arr, cmap="gray", vmin= 0, vmax= 255)
    # plt.show()

def zadanie3i4(arr1, arr2):
    _, (left, right) = plt.subplots(1, 2)
    common_args = {"cmap": "gray", "vmin": 0, "vmax": 255}
    left.imshow(arr1, **common_args)
    right.imshow(arr2, **common_args)
    plt.show()

def zadanie5(bri, con):
    _, axes = plt.subplots(1, 3)
    arr0 = np.random.randint(0, 256, (100,100), dtype=np.uint8)
    arr1 = np.clip(arr0.astype(np.uint16) * con,0,255)
    arr2 = np.clip(arr0.astype(np.uint16) + bri, 0, 255)
    common_args = {"cmap": "gray", "vmin": 0, "vmax": 255}
    axes[0].imshow(arr0, **common_args)
    axes[1].imshow(arr1, **common_args)
    axes[2].imshow(arr2, **common_args)
    plt.show()
def zadanie6(low,high):
    arr = np.random.randint(0, 256, (100, 100), dtype=np.uint8)
    arr2=arr.copy()
    arr2[arr<low]=0
    arr2[arr>high]=255
    zadanie3i4(arr,arr2)

def zadanie7():
    arr = np.random.randint(0, 256, (100, 100), dtype=np.uint8)
    arr[40:60,40:70] = 255
    plt.imshow(arr, cmap="gray", vmin= 0, vmax= 255)
    plt.show()

def zadanie8():
    arr = np.random.randint(0, 256, (100, 100), dtype=np.uint8)
    arr[40:60, 40:70] = 255

    arr = 255 - arr

    plt.imshow(arr, cmap="gray", vmin= 0, vmax= 255)
    plt.show()

def zadanie9():
    arr = np.linspace(0,255,100)
    arr = np.tile(arr,(100,1))
    plt.imshow(arr, cmap="gray", vmin=0, vmax=255)
    plt.show()

def zadanie10():
    x=np.linspace(0, 2 * math.pi * 50, 1000)
    y=np.sin(x)
    plt.plot(x,y)
    plt.show()

if __name__ == '__main__':
    #zadanie3i4(zadanie3(), zadanie4())
    # zadanie5(150, 1.8)
    zadanie10()