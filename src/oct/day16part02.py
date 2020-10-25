import random


def random_sum():
    # Create a program that adds random numbers between 10 and 30. As soon as
    # the number 15 or 25 comes the program is terminated and the sum of the
    # previous numbers gets printed

    sum = 0
    looping = True

    while looping:
        random_number = random.randint(10, 30)

        if (random_number == 15 or random_number == 25):
            looping = False
            break
        else:
            print("+ " + str(random_number))
            sum += random_number
    
    print("=====")
    print(sum)
