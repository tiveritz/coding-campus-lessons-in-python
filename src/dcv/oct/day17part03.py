from time import sleep
from random import randint


# Write a console game that randomly moves a guy between two walls. If the guy
# hits the wall, the game is over. Probabilities of movements are 30% left or
# right, 40% stay
# let the user choose the game width with a user input

GUY = [" ö ", "/|\\", "/ \\"]

def walking_guy():
    field_width = user_input()
    pos = field_width // 2

    while True:

        if (pos == 0 or pos == field_width):
            break
        
        print_guy(pos, field_width)
        pos = new_pos(pos)
        sleep(.5)

def user_input():
    while True:
        user_input = input("Welcom to the walking_guy game. Enter the field width: ")
        if user_input.isdigit():
            break

    return int(user_input)

def new_pos(pos):
    chance = randint(0, 9)

    if chance <= 2:
        pos += 1
    elif chance >= 7:
        pos -= 1
    
    return pos

def print_guy(pos, width):
    for body_part in GUY:
        print("|" + pos * " " + body_part + (width - pos) * " " + "|")
