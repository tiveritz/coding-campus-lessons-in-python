# Print the pascal's triangle
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1

def pascal(rows):
    for row in range(1, rows+2):
        for col in range(1, row+1):
            res = pascal_calc(row, col)
            print(str(res) + " ", end = '')
        print()

def pascal_calc(row, col):
    if (col == 1 or col == row):
        return 1
    return pascal_calc(row - 1, col - 1) + pascal_calc(row - 1, col)



# Additional task: implement a caching, to accelerate the program

def pascal_with_caching(rows):
    # Declare cache and fill with 0
    cache = [[0 for i in range(rows+1)] for i in range(rows+1)]

    for row in range(1, rows+2):
        for col in range(1, row+1):
            res = pascal_calc_caching(row, col, cache)
            print(str(res) + " ", end = '')
        print()

def pascal_calc_caching(row, col, cache):
    if (cache[row - 1][col - 1] != 0):
        return cache[row - 1][col - 1]
    if (col == 1 or col == row):
        return 1
    res = pascal_calc_caching(row - 1, col - 1, cache) + pascal_calc_caching(row - 1, col, cache)
    cache[row - 1][col - 1] = res
    return res
