# You are trying to determine which of two apartments has a larger
# balcony. Both balconies are rectangles, and you have the length and
# width, but you need the area.
#
# Task 
# Evaluate the area of two different balconies and determine which one
# is bigger.
# 
# Input Format 
# Your inputs are two strings where the measurements for height and
# width are separated by a comma. The first one represents apartment A,
# the second represents apartment B.
# 
# Output Format: 
# A string that says whether apartment A or apartment B has a larger
# balcony.
# 
# Sample Input 
# '5,5'
# '2,10'
# 
# Sample Output 
# Apartment A

class Balcony():

    def __init__(self, measurements):
        self.width = int(measurements.split(',')[0])
        self.height = int(measurements.split(',')[1])
    
    def area(self):
        return self.width * self.height
    
    def __gt__(self, other):
        if (self.area() > other.area()):
            return True
        return False


balcony_ap_a = Balcony(input())
balcony_ap_b = Balcony(input())

if balcony_ap_a > balcony_ap_b:
    print('Apartment A')
else:
    print('Apartment B')
