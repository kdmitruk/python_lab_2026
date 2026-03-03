#import math
from math import sin, radians
from random import uniform
GRAVITY = 9.81
LENGTH = 80
SCALE = 2
IMPACT_RADIUS = 2

def calculate_impact(angle, speed, player):
    return speed ** 2 * sin(radians(angle * 2)) / GRAVITY + player

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
    shooter = player1
    target = player2
    while True:
        print(f"{"First" if shooter == player1 else "Second"} player is up:")
        angle,speed = get_input()
        if shooter == player2:
            angle = 180-angle
        z = calculate_impact(angle, speed, shooter)
        print(z)
        display(z,player1,player2)
        shooter, target = target, shooter

def display(z,player1,player2):
    def scaled(pos):
        return round(pos/SCALE)
    ground = ["_"]*LENGTH
    ground[scaled(player1)] = "1"
    ground[scaled(player2)] = "2"
    try:
        ground[scaled(z)] = "X"
    except IndexError:
        print("Out of screen.")
    [print(symbol, end = "") for symbol in ground]
    print()

def start_game():
    player1 = uniform(1,LENGTH/2)*SCALE
    player2 = uniform(LENGTH/2,LENGTH-1)*SCALE
    return player1,player2
if __name__ == '__main__':
    main()
