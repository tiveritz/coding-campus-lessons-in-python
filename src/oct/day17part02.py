import math


def round_floats():
    floats = [1.0, 1.15, 1.9, 11.0, 19.0, 120.0]

    for f in floats:
        print(f, end = " ")
        print(round(f), end = " ")
        print(math.floor(f), end = " ")
        print(math.ceil(f), end = " ")
        print()

    for f in floats:
        print(f, end = " ")
        print(round(f, 1), end = " ")
        print(math.floor(f * 10) / 10, end = " ")
        print(math.ceil(f * 10) / 10, end = " ")
        print()