# Output simple multiplication from 1x1 to 9x9
def simple_multiplication():
    mult_result = 0

    for multiplier in range(1, 10):
        for multiplicand in range(1, 10):
            mult_result = multiplier * multiplicand
            print(str(multiplier) + " * " + str(multiplicand) + " = " + str(mult_result))


# Output all primes from 0 to 100
def primes():
    primes = 100

    for prime in range(0, primes + 1):
        if prime > 1:
            for i in range(2, prime):
                if (prime % i == 0):
                    break
            else:
                print(prime)


# Test if a given word is a palindrome
def palindrom():
    word = "anna"
    print(word == word[::-1]) # Don't know what this is? -> list slicing


# Hello World Lists
def hello_world_list():
    my_strings = ["A", "U", "L", "O", "E", "D", "P", "A", "F", "B"]
    my_numbers = ["2", "1", "8", "5", "6", "9", "3", "9", "4", "8"]

    for string in my_strings:
        print(string)

    for number in my_numbers:
        print(number)


# simple_multiplication()
# primes()
# palindrom()
# hello_world_list()
