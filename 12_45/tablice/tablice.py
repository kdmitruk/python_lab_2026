from filecmp import cmp
from pickletools import uint8

import numpy as np
import matplotlib.pyplot as plt

def show(*imgs):
    size = len(imgs)
    _, axes = plt.subplots(1, size)
    kwargs = {"cmap": 'summer', "vmin": 0, "vmax": 255}
    if size == 1:
        axes.imshow(imgs[0], **kwargs)
    else:
        for i in range(len(imgs)):
            axes[i].imshow(imgs[i], **kwargs)

    plt.show()

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
    return arr

def zad3():
    arr = np.random.randint(0,256,(100,100),dtype=np.uint8)
    return arr

def zad4():
    arr = np.random.normal(128,50,(100,100))
    return arr

if __name__ == '__main__':
   # zad1()
   #  zad2()
   #  zad3()
   show(zad3(), zad4())