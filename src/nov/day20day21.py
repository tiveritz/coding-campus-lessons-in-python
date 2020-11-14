def canvas_shapes():
    canvas = new_canvas(28, 28, " ")
    print_canvas(canvas)

    # Print square with defined starting point
    x_min_square = 6
    y_min_square = 4
    l_square = 6
    print_canvas(get_canvas_with_square(canvas, x_min_square, y_min_square, l_square))




# ------------------------------------------------------------------------------
def new_canvas(rows, cols, char):
    return [[char for col in range(cols)] for row in range(rows)]

def print_canvas(canvas):
    print("y")
    print("↑")
    for row in canvas:
        print("|", end = "")
        for col in row:
            print(col, end = " ")
        print()
    print(" " + "-"*(len(canvas[0]) * 2) + "→ x" + "\n\n")

def get_canvas_with_square(old_list, x_min, y_min, length):
    square = square = y = [row[:] for row in old_list]

    col_max_index = x_min + length
    row_max_index = y_min + length

    for row in range(row_max_index):
        for col in range(col_max_index):
            is_in_row = row >= y_min and row < row_max_index
            is_in_col = col >= x_min and col < col_max_index

            if (is_in_row and is_in_col):
                square[row][col] = "·"

    return square

canvas_shapes()