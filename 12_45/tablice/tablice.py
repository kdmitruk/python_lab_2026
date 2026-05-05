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

def zad5(image,brightness,contrast):

    image1=np.clip(image.astype(np.int16)*contrast,0,255)
    image2= np.clip(image.astype(np.int16) + brightness,0,255)

    return image,image1, image2

def zad6(image,low,high):
    image1 = image.copy()
    image1[image < low] = low
    image1[image > high] = high
    return image,image1

def zad7(image,top,left,bottom,right):
    image[top:bottom,left:right] = 255
    return  image

def zad8(image):
    return 255 - image

def zad9():
    arr = np.linspace(0,255,100)
    arr = np.tile(arr,(100,1))
    return arr

if __name__ == '__main__':
   # zad1()
   # zad2()
   # zad3()
   # show(*zad5(zad3(),-50,1.5))
   # show(*zad6(zad3(),100,150))
   # show(zad7(zad3(),10,20,30,40))
   # show(zad8(zad7(zad3(),10,20,30,40)))
    show(zad9())