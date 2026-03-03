#import math
from math import sin, radians

GRAVITY = 9.81

def calculate_impact(angle, velocity):
    return velocity**2 * sin(radians(angle)*2) / GRAVITY

def get_input():
    while True :
        angle = float(input("Kąt: "))
        if angle <= 0 or angle >= 90:
            print("Wartość nie jest odpowiednia!")
        else:
            break

    velocity = float(input("Prędkość początkowa: "))
    return angle, velocity

def main():
    while True:
        angle, velocity = get_input()
        print(velocity)
        print(angle)

        z = calculate_impact(angle, velocity)
        print(z)


if __name__ == '__main__':
    main()



