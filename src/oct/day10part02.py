# In bowling there are 10 pins (not 9). Try to categorize the throws:
# 1 - 3 OK
# 4 - 6 Nice throw
# 7 - 9 Very nice throw
# 10 Strike

def bowling():
    bowl_throw = 10

    # In python there is no switch statement. As an alternative you can
    # use a dictionary (I packet this in a seperate function)
    print(get_throw_message(bowl_throw))

def get_throw_message(count):
    switch = {
        1 : 'OK',
        2 : 'OK',
        3 : 'OK',
        4 : 'Nice throw',
        5 : 'Nice throw',
        6 : 'Nice throw',
        7 : 'Very nice throw',
        8 : 'Very nice throw',
        9 : 'Very nice throw',
        10 : 'Strike',
    }
    return switch.get(count, "Invalid count")
