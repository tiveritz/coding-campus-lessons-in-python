import random

def random_repetition():
    cars = ["Audi", "BMW", "Mercedes", "Seat", "Volkswagen"]

    for i in range(10):
        random_index = random.randint(0, len(cars) - 1)
        print(cars[random_index])
