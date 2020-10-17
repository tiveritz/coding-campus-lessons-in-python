# Calculate the sum of the numbers from 1 to 1000
def my_sum():
    my_sum = 0
    i = 1

    while (i <= 1000):
        my_sum += i
        i += 1

    print(my_sum)


# Calculate the factorial of 20
def factorial():
    factorial = 20
    multiplikation = 1
    i = 1

    while (i <= factorial):
        multiplikation *= i
        i += 1

    print(multiplikation)


# Calcolaute PI's approximation with the formula 4 - 4/3 + 4/5 - 4/7 ...
def pi_approx():
    numerator = 4
    denominator = 1
    approx_level = 10
    pi_approx = 0

    i = 0
    while (i < approx_level):
        pi_approx += (numerator / denominator)
        denominator += 2
        pi_approx -= (numerator / denominator)
        denominator += 2
        i += 1

    print(pi_approx)


# Output a square of letters
def square_with_letters():
    letter = "A"
    square_size = 5

    for i in range(0, square_size):
        print(letter * square_size)


# Output an arrow
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

def output_arrow():
    arrow_len = 5
    arrow_text = "*"

    i = 1
    while (i <= arrow_len):
        print(arrow_text * i)
        i += 1
    
    i = arrow_len -1
    while (i >= 1):
        print(arrow_text * i)
        i -= 1
    
    # Solution with single loop
    looping = True
    rising = True
    i = 1

    while looping:
        print(arrow_text * i)

        if (i == arrow_len):
            rising = False
        if (i == 0):
            looping = False

        if rising:
            i += 1
        else:
            i -= 1
