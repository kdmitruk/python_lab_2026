#import math
from math import sin, radians
GRAVITY = 9.81


def calculate_impact(angle, speed):
    return speed ** 2 * sin(radians(angle * 2)) / GRAVITY



def get_input():
    while True:
        angle = float(input("angle "))
        if angle > 90 or angle < 0:
            print("Improper angle")
        else:
            break

    speed = float(input("speed "))
    return angle,speed
def main():
    angle,speed = get_input()
    z = calculate_impact(angle, speed)
    print(z)

if __name__ == '__main__':
    main()
