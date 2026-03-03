#import math
from math import sin, radians
GRAVITY = 9.81
LENGTH = 80
SCALE = 2

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
    display(z)

def display(z):
    ground = ["_"]*LENGTH
    ground[round(z/SCALE)] = "X"
    [print(symbol, end = "") for symbol in ground]
    """for symbol in ground:
        print(symbol, end = "")"""
    """    for i in range(LENGTH):
        if i == round(z/SCALE):
            print("X", end = "")
        else:
            print("_", end = "")"""

if __name__ == '__main__':
    main()
