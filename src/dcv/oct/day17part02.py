from math import floor, ceil


def round_floats():
    floats = [1.0, 1.15, 1.9, 11.0, 19.0, 120.0]

    for f in floats:
        print(f, end = " ")
        print(round(f), end = " ")
        print(floor(f), end = " ")
        print(ceil(f), end = " ")
        print()

    for f in floats:
        print(f, end = " ")
        print(round(f, 1), end = " ")
        print(floor(f * 10) / 10, end = " ")
        print(ceil(f * 10) / 10, end = " ")
        print()