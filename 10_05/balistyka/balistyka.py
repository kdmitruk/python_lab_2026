#import math
from math import sin, radians

GRAVITY = 9.81
while True :
    angle = float(input("Kąt: "))
    if angle <= 0 or angle >= 90:
        print("Wartość nie jest odpowiednia!")
    else:
        break

velocity = float(input("Prędkość początkowa: "))

print(velocity)
print(angle)

z = velocity**2 * sin(radians(angle)*2) / GRAVITY
print(z)