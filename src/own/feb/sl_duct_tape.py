# -- DUCT TAPE ---------------------------------------------------------
# You want to completely cover a flat door on both sides with duct tape.
# You need to know how many rolls of duct tape to buy when you go to the
# store.
# 
# Task: 
# Given the height and width of the door, determine how many rolls of
# duct tape you will need (a roll of duct tape is 60 feet long and 2
# inches wide and there are 12 inches in each foot). Don't forget both
# sides of the door!
# 
# Input Format: 
# Two integers that represent the height and width of the door.
# 
# Output Format: 
# An integer that represents the total rolls of duct tape that you need
# to buy.
# 
# Sample Input: 
# 7
# 4
# 
# Sample Output: 
# 6

import math


class DuctTape():
    '''
    A class to represent a duct tape roll

    Attributes
    ----------
    length : int
        Length of the duct tape roll in inches
    width : int
        Width of the duct tape roll in inches

    Methods
    -------
    area():
        Returns the total area of the duct tape roll
    '''
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Door():
    '''
    A class to represent a door

    Attributes
    ----------
    length : int
        Length of the door in inches
    width : int
        Width of the door in inches

    Methods
    -------
    two_side_area():
        Returns the total area of the door (both sides)
    '''

    def __init__(self, length, width):
        self.length = length * 12
        self.width = width * 12
    
    def two_side_area(self):
        return 2 * self.length * self.width


def calc_required_duct_tape_rolls(area, duct_tape):
    duct_tape_area = duct_tape.area()

    return math.ceil(area / duct_tape_area)


duct_tape_length = 60 * 12 # 60feet long
duct_tape_width = 2

duct_tape_roll = DuctTape(duct_tape_length, duct_tape_width)
door = Door(int(input()), int(input()))

print(calc_required_duct_tape_rolls(door.two_side_area(), duct_tape_roll))
