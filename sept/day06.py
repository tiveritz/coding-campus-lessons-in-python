from math import ceil

def hello_world_recursion(n):
    # Recherchiere Recursion

    if (n == 0):
        print("End of Recursion")
    else:
        print("Recursion number " + str(n))
        n -= 1
        hello_world_recursion(n)


# Declare global variables for sorting algorithm
compare_counter = 0
swap_counter = 0

def merge_sort():
    # Informiere dich über den MergeSort Sortieralgorithmus und setze
    # sie in Python um.
    # Vergleiche auch die Komplexität, indem du bei jedem Zugriff auf das
    # Array einen Counter erhöhst und diesen am Ende mit ausgiebst.

    arr = [6, 23, 78, 34, 89, 2, 56, 78, 6, 30, 27, 81, 7, 7, 84, 20, 19]

    print(arr)
    print(merge_sort_algorithm(arr))

    print("Comparisons: " + str(compare_counter))
    print("Swaps: " + str(swap_counter))


def merge_sort_algorithm(arr):

    sorted_arr = arr
    global compare_counter
    global swap_counter

    if (len(arr) > 1):
        half_index = ceil(len(arr) / 2)

        left, right = [], []

        for i in range(half_index):
            left.append(sorted_arr[i])

        for j in range(half_index, len(arr)):
            right.append(arr[j])

        left = merge_sort_algorithm(left)
        right = merge_sort_algorithm(right)

        i = 0
        j = 0
        k = 0

        while (k < len(sorted_arr)):
            compare_counter += 1
            if (i < len(left) and j < len(right)):
                if (left[i] < right[j]):
                    sorted_arr[k] = left[i]
                    swap_counter += 1
                    i += 1
                else:
                    sorted_arr[k] = right[j]
                    swap_counter += 1
                    j += 1
            else:
                if (i == len(left)):
                    sorted_arr[k] = right[j]
                    swap_counter += 1
                    j += 1
                else:
                    sorted_arr[k] = left[i]
                    swap_counter += 1
                    i += 1
            k += 1

    return sorted_arr

# hello_world_recursion(5)
# merge_sort()