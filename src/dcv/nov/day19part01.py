from random import randint


def hello_world_tow_dimensional_array():
    # Empty list with 7 rows and 7 cols
    my_list = [["" for i in range(7)] for i in range(7)]

    print(my_list)

    # But since lists do not work like arrays it is not required to pre-define
    # the length of the list, so you could also write;
    # Basically just append lists as you need them

    my_list_2 = []

    for row in range(7):
        my_list_2.append([])
        for col in range(7):
            my_list_2[row].append(randint(0,21))

    print(my_list_2)

    # Easy way of printing a two dimensional array as a table:
    for row in my_list_2:
        for col in row:
            print('{:2}'.format(col), end = "  ")
        print()
    
    # Example: print row sums
    for row in my_list_2:
        row_sum = 0
        for col in row:
            row_sum += col
        print(row_sum)
