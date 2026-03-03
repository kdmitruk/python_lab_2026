#import math
from math import sin, radians
from random import uniform
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
    player1,player2 = start_game()
    angle,speed = get_input()
    z = calculate_impact(angle, speed)
    print(z)
    display(z,player1,player2)

def display(z,player1,player2):
    def scaled(pos):
        return round(pos/SCALE)
    ground = ["_"]*LENGTH
    ground[scaled(player1)]= "1"
    ground[scaled(player2)]= "2"
    ground[scaled(z)] = "X"
    [print(symbol, end = "") for symbol in ground]

def start_game():
    player1 = uniform(1,LENGTH/2)*SCALE
    player2 = uniform(LENGTH/2,LENGTH-1)*SCALE
    return player1,player2
if __name__ == '__main__':
    main()
