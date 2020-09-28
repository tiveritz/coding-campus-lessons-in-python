def selection_sort():
    # Inform youself about SelectionSort sorting algoritm and program it in
    # Python.
    # Compare complexity by counting array access

    # Declare the list
    sort = [6, 23, 78, 34, 89, 2, 56, 78, 6, 30, 27, 81, 7, 7, 84, 20]

    compare_counter = 0
    swap_counter = 0
    to_swap = False
    min_element = 0
    min_element_idx = 0

    for i in range(len(sort)):
        to_swap = False
        min_element = sort[i]
        
        for j in range(i+1, len(sort)):
            compare_counter += 1
            if sort[j] < min_element:
                min_element = sort[j]
                min_element_idx = j
                to_swap = True
        
        if to_swap:
            swap_counter += 1
            sort[i], sort[min_element_idx] = sort[min_element_idx], sort[i]

    print(sort)
    print(compare_counter)
    print(swap_counter)


def bubble_sort():
    # Inform youself about BubbleSort sorting algoritm and program it in
    # Python.
    # Compare complexity by counting array access

    # Declare the list
    sort = [6, 23, 78, 34, 89, 2, 56, 78, 6, 30, 27, 81, 7, 7, 84, 20]

    compare_counter = 0
    swap_counter = 0
    to_swap = True

    while to_swap:
        to_swap = False
        for i in range(1, len(sort)):
            compare_counter += 1
            if (sort[i - 1] > sort[i]):
                to_swap = True
                swap_counter += 1
                sort[i - 1], sort[i] = sort[i], sort[i - 1]
    
    print(sort)
    print(compare_counter)
    print(swap_counter)


# selection_sort()
# bubble_sort() 

