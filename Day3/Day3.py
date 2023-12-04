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


def get_numbers(input_file):
    matrix = create_matrix(get_input_proportions(input_file)["x"], get_input_proportions(input_file)["y"])
    numbers = []
    is_building_number = False
    number_start = matrix.get_point(0, 0)
    prev_point = matrix.get_point(0, 0)

    for line in matrix.matrix:
        for point in line:
            if point.value.isdigit() and not is_building_number:
                number_start = point
                is_building_number = True

            if not point.value.isdigit():
                if is_building_number:
                    number_end = prev_point
                    is_building_number = False
                    number = Number(matrix, number_start, number_end)
                    numbers.append(number)
            else:
                prev_point = point

def solve_part1():
    pass