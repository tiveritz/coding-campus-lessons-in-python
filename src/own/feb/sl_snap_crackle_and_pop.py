# You have six bowls of Rice Krispies in front of you, and they make
# different noises when you pour milk over them based on the total
# number of Rice Krispies in each bowl.
# If a bowl has a number of Rice Krispies that is divisible by 3, it
# will make a Pop sound. If it is not divisible by 3 but is odd it will
# make a Snap sound.  If it is not divisible by 3, but it is even, it
# will make a Crackle sound.
# 
# Task: 
# Based on the quantities in each bowl, output the noise that they make.
# 
# Input Format: 
# You receive 6 integers and each integer represents the number of Rice
# Krispies in your bowls.
# 
# Output Format: 
# You should output a string with the sounds made by each bowl separated
# by spaces in the order that they were input.
# 
# Sample Input: 
# 18
# 5
# 100
# 25
# 40
# 24
# 
# Sample Output: 
# Pop Snap Crackle Snap Crackle Pop

class RiceKrispieBowl():
    '''
    A class to represent a bowl of rice krispie with rice crispies in it

    Attributes
    ----------
    rice_krispies_count : int
        The amount of rice krispies in the basket

    Methods
    -------
    get_sound():
    Returns a string with the sound the bowl makes when you pour milk
    over it 
    '''
    def __init__(self, rice_krispies_count):
        self.rice_krispies_count = rice_krispies_count
    
    def get_sound(self):
        if self.rice_krispies_count % 3 == 0:
            return 'Pop'
        elif self.rice_krispies_count % 2 != 0:
            return 'Snap'
        else:
            return 'Crackle'

rice_krispies = []

for i in range(0,6):
    rice_krispies_count = int(input())
    rice_krispies.append(RiceKrispieBowl(rice_krispies_count))

for rice_krispie in rice_krispies:
    print(rice_krispie.get_sound(), end=' ')
