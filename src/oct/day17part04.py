# Look how ridiculously easy it is to get user input in Python

def hello_world_user_input():
    while True:
        age = input("Enter your age: ")
        if age.isdigit():
            break
        else:
            print("Not a number, try again")

    print("You are " + age + " old")
