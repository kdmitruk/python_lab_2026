#import math
from math import sin, radians
GRAVITY = 9.81

while True:
    angle = float(input("angle "))
    if angle > 90 or angle < 0:
        print("Improper angle")
    else:
        break

speed = float(input("speed "))

print(angle)
print(speed)

z = speed**2 * sin(radians(angle * 2))/GRAVITY

print(z)