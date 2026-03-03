#import math
from math import sin, radians
from random import uniform

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

def print_impact(impact, pos1, pos2):
    scaled_impact = round(impact*SCALE)
    ground = ["_"]*LENGTH
    ground[scaled_impact] = "X"
    ground[pos1] = "1"
    ground[pos2] = "2"
    [print(symbol, end="") for symbol in ground]
    print()

def start_game():
    start1 = uniform(0,LENGTH/2)
    start2 = uniform(LENGTH/2+1, LENGTH)
    return round(start1), round(start2)

def main():
    pos1, pos2 = start_game()
    while True:
        angle, velocity = get_input()
        print(velocity)
        print(angle)

        z = calculate_impact(angle, velocity)
        print(z)
        print_impact(z,pos1, pos2)


if __name__ == '__main__':
    main()



