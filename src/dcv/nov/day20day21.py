from math import sqrt, ceil


def canvas_shapes():
	canvas = new_canvas(28, 28, " ")

	# Print square with defined starting point
	x_min_square = 6
	y_min_square = 4
	l_square = 6
	print_canvas(get_canvas_with_square(canvas, l_square, x_min_square, y_min_square))

	# Print square into the center of the canvas
	print_canvas(get_canvas_with_square(canvas, l_square))

	# Print line
	P1x_line = 3
	P1y_line = 2
	P2x_line = 15
	P2y_line = 19
	print_canvas(get_canvas_with_line(canvas, P1x_line, P1y_line, P2x_line, P2y_line))

	# Print triangle with defined center coordinates
	x_center_triangle = 8
	y_center_triangle = 6
	l_triangle = 14
	print_canvas(get_canvas_with_triangle(canvas, l_triangle, x_center_triangle, y_center_triangle))

	# Print triangle into center of the canvas
	print_canvas(get_canvas_with_triangle(canvas, l_triangle))

	# Print circle with defined center coordinates
	x_center_circle = 10
	y_center_circle = 10
	radius = 10
	print_canvas(get_canvas_with_circle(canvas, radius, x_center_circle, y_center_circle))

	# Print circle into center of canvas
	print_canvas(get_canvas_with_circle(canvas, radius))


# ------------------------------------------------------------------------------
def new_canvas(rows, cols, char):
	return [[char for col in range(cols)] for row in range(rows)]

def print_canvas(canvas):
	print("y")
	print("↑")
	for row in canvas[::-1]:
		print("|", end = "")
		for col in row:
			print(col, end = " ")
		print()
	print(" " + "-"*(len(canvas[0]) * 2) + "→ x" + "\n\n")

def get_canvas_with_square(canvas, length, x_min = None, y_min = None):
	square = [row[:] for row in canvas]
	if x_min == None:
		x_min = special_round(len(square) / 2 - length / 2)
	if y_min == None:
		y_min = special_round(len(square[0]) / 2 - length / 2)

	col_max_index = x_min + length
	row_max_index = y_min + length

	for row in range(row_max_index):
		for col in range(col_max_index):
			is_in_row = row >= y_min and row < row_max_index
			is_in_col = col >= x_min and col < col_max_index

			if (is_in_row and is_in_col):
				square[row][col] = "·"

	return square

def get_canvas_with_line(canvas, P1x, P1y, P2x, P2y, copy_array = True):
	line = canvas

	if copy_array:
		line = [row[:] for row in canvas]

	k = (P2y - P1y) / (P2x - P1x)
	d = 1.0 * P1y - k * P1x

	# Add points with y(x) = k * x + d
	loop_start_x = min(P1x, P2x)
	loop_end_x = max(P1x, P2x)

	for x in range(loop_start_x, loop_end_x + 1):
		y = special_round(k * x + d)
		line[y][x] = "·"

	# Add points with x(y) = (y - d) / k
	loop_start_y = min(P1y, P2y)
	loop_end_y = max(P1y, P2y)

	for y in range(loop_start_y, loop_end_y):
		x = special_round((y - d) / k)
		line[y][x] = "·"

	return line

def get_canvas_with_triangle(canvas, length, x_center = None, y_center = None):
	triangle = [row[:] for row in canvas]

	if x_center == None:
		x_center = special_round(len(triangle) / 2)
	if y_center == None:
		y_center = special_round(len(triangle[0]) / 2)

	height = sqrt(length**2 - (length / 2)**2)
	x_min = special_round(x_center - length / 2)
	y_min = special_round(y_center - height / 2)

	P3x = x_min
	P3y = y_min
	
	P2x = x_min + length-1
	P2y = y_min

	P1x = special_round(x_min + length / 2)
	P1y = special_round(y_min + height-1)

	get_canvas_with_line(triangle, P1x, P1y, P2x, P2y, False)
	get_canvas_with_line(triangle, P2x, P2y, P3x, P3y, False)
	get_canvas_with_line(triangle, P3x, P3y, P1x, P1y, False)

	return triangle

def special_round(number):
	if (float(number) % 1) >= 0.5:
		return ceil(number)
	else:
		return round(number)

def get_canvas_with_circle(canvas, r, x_center = None, y_center = None):
	circle = [row[:] for row in canvas]

	if x_center == None:
		x_center = special_round(len(circle) / 2)
	if y_center == None:
		y_center = special_round(len(circle[0]) / 2)

	# Add the points with y(x) = ±sqrt(r^2 - (x-a)^2) + b
	loop_start_x = x_center - r
	loop_end_x = x_center + r

	for x in range(loop_start_x, loop_end_x + 1):
		point = sqrt(r**2 - (x - x_center)**2)
		y_pos = special_round(point + y_center)
		y_neg = special_round(-point + y_center)

		circle[y_pos][x] = "·"
		circle[y_neg][x] = "·"

	# Add the points with x(y) = ±sqrt(r^2 - (y - b)^2) + a
	loop_start_y = y_center - r
	loop_end_y = y_center + r

	for y in range(loop_start_y, loop_end_y + 1):
		point = sqrt(r**2 - (y - y_center)**2)
		x_pos = special_round(point + y_center)
		x_neg = special_round(-point + y_center)

		circle[y][x_pos] = "·"
		circle[y][x_neg] = "·"
	
	return circle

canvas_shapes()