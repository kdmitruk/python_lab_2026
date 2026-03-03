#import math
from math import sin, radians

GRAVITY = 9.81
SCALE = 0.9
LENGTH = 80

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

def print_impact(impact):
    scaled_impact = round(impact*SCALE)
    print(scaled_impact)
    '''for i in range(0,LENGTH):
        if i == scaled_impact:
            print("X", end="")
        else:
            print("_", end="")
    print()'''
    ground = ["_"]*LENGTH
    ground[scaled_impact] = "X"
    '''
    for symbol in ground:
        print(symbol, end="")
    '''
    [print(symbol, end="") for symbol in ground]
    print()



def main():
    while True:
        angle, velocity = get_input()
        print(velocity)
        print(angle)

        z = calculate_impact(angle, velocity)
        print(z)
        print_impact(z)


if __name__ == '__main__':
    main()



