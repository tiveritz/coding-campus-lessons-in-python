# You go hunting for Easter eggs with a friend. You think that you have
# found all of the eggs, but you want to make sure that you don't leave
# any behind! Compare Easter baskets with your friend to decide if you
# should keep hunting.
# 
# Task: 
# If you know the total number of eggs that were hidden and the amount
# in both of your baskets. Evaluate whether it is time to eat candy or
# keep hunting for more eggs.
# 
# Input Format: 
# Three integer values. The first represents the total number of eggs,
# the second, the amount in your basket, and lastly the amount that your
# friend has found.
# 
# Output Format: 
# A string that says 'Keep Hunting' if there are still eggs out there or
# 'Candy Time' if you found all the eggs.
# 
# Sample Input:
# 100
# 40
# 60
# 
# Sample Output: 
# Candy Time

class Basket():
    '''
    A class to represent a basket with items in it

    Attributes
    ----------
    items_count : int
        The amount of items in the basket

    Methods
    -------
    __add__(self, other)
        Returns the combined amount of items in the baskets 
    
    add_items(count)
        Adds the passed amount of items to the basket
    '''

    def __init__(self):
        self.items_count = 0
    
    def __add__(self, other):
        return self.items_count + other.items_count
    
    def add_items(self, count):
        self.items_count += count


my_basket = Basket()
his_basket = Basket()

egg_count = int(input())
my_basket.add_items(int(input()))
his_basket.add_items(int(input()))

if (my_basket + his_basket) < egg_count:
    print('Keep Hunting')
else:
    print('Candy Time')
