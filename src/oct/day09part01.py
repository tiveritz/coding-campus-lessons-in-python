def bubble_sort(arr):
    sorted = arr.copy()
    to_swap = True

    while to_swap:
        to_swap = False
        for i in range(1, len(arr)):
            if (sorted[i - 1] > sorted[i]):
                to_swap = True
                sorted[i - 1], sorted[i] = sorted[i], sorted[i - 1]
    return sorted

def hello_world_functions():
    my_array = [6, 23, 78, 34, 89, 2, 56, 78, 6, 30, 27, 81, 7, 7, 84, 20]

    # function call. Note the passed parameter (my_array)
    print(bubble_sort(my_array))
    print(my_array) # original array remained untouched

    # Another example
    my_array2 = [-2, -9, 5, 9, 5, 2, 4, -3, 8, -6, 4, 6]
    print(bubble_sort(my_array2))
    print(my_array2)
