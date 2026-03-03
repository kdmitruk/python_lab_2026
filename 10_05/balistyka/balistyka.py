#import math
from math import sin, radians
from random import uniform


GRAVITY = 9.81
SCALE = 0.9
LENGTH = 80
IMPACT_RADIUS = 2

def calculate_impact(angle, velocity, offset):
    return velocity**2 * sin(radians(angle)*2) / GRAVITY + offset

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
    ground[pos1] = "1"
    ground[pos2] = "2"
    try:
        ground[scaled_impact] = "X"
    except IndexError:
        print("Poza skalą")
    [print(symbol, end="") for symbol in ground]
    print()

def start_game():
    start1 = uniform(0,LENGTH/2)
    start2 = uniform(LENGTH/2+1, LENGTH)
    return round(start1), round(start2)

def check_hit(impact, pos):
    return abs(impact - pos) <= IMPACT_RADIUS

def main():
    pos1, pos2 = start_game()
    shooter = pos1
    target = pos2
    while True:
        print("Gracz: ", 1 if shooter == pos1 else 2)
        angle, velocity = get_input()

        z = calculate_impact(angle, velocity, shooter/SCALE)

        print_impact(z,pos1, pos2)
        if check_hit(z, target/SCALE):
            break
        shooter,target = target,shooter


if __name__ == '__main__':
    main()



