from Matrix import *
from Number import *
INPUT_FILE = open("Day3Input.txt")


def get_input_proportions(input_file):
    INPUT_FILE.seek(0)
    input_as_list = []
    for line in input_file:
        input_as_list.append(line.strip())

    return {"x": len(input_as_list[0]), "y": len(input_as_list)}


def create_matrix(len_x, len_y):
    matrix = Matrix(len_x, len_y)
    INPUT_FILE.seek(0)
    for y, line in enumerate(INPUT_FILE):
        for x, char in enumerate(line.strip()):
            matrix.set_value(x, y, char)

    return matrix


input_proportions = get_input_proportions(INPUT_FILE)
matrix_len_x = input_proportions["x"]
matrix_len_y = input_proportions["y"]

m = create_matrix(matrix_len_x, matrix_len_y)
for point in m.matrix:
    number_started = False
    if point.value.isdigit():
        if not number_started:
            number_start = point
            number_started = True
    else:
        number_started = False
        number_end = point
        # number = Number(m, point)