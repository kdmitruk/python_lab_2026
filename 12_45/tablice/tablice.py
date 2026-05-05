from filecmp import cmp

import numpy as np
import matplotlib.pyplot as plt

def zad1():
    arr = np.array(
        [[1, 2, 8, 46, 26], [110, 64, 32, 5, 0]],
        dtype = np.uint8
    )
    print(arr)
    print(arr.shape)

def zad2():
    arr = np.zeros((100,100),dtype=np.uint8)
    arr[50,20]=255

    plt.imshow(arr,cmap='gray')
    plt.show()

if __name__ == '__main__':
   # zad1()
    zad2()
