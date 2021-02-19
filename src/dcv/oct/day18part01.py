def function_repetition():
    # Calls all the examples
    
    # Call Hello + a name
    name1 = "Lukas"
    name2 = "Alex"
    print_hello_world(name2)

    # Create a new string with Hi + a name
    new_name_string = create_string(name1)
    print(new_name_string)

    print(create_string(name1)) # same thing than above in one line

    # Square a number
    print(square(3))
    print(square(3) + 2)

    # Call a function in a function
    print(multiply_square(2))

def print_hello_world(name_within_function_scope):
    print("Hello " + name_within_function_scope)

def create_string(name):
    new_string = "Hi " + name
    return new_string

def square(number):
    return number * number

def multiply_square(number):
    return square(number) * square(number)
