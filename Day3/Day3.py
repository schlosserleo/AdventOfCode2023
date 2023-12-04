from Matrix import *
from Number import *


def get_input_proportions(input_file):
    input_file.seek(0)
    input_as_list = []
    for line in input_file:
        input_as_list.append(line.strip())

    return {"x": len(input_as_list[0]), "y": len(input_as_list)}


def fill_matrix(input_file, len_x, len_y):
    matrix = Matrix(len_x, len_y)
    input_file.seek(0)
    for y, line in enumerate(input_file):
        for x, char in enumerate(line.strip()):
            matrix.set_value(x, y, char)

    return matrix


def get_numbers(matrix):
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
    return numbers


def solve_part1(matrix, numbers):
    result_sum = 0
    number_is_valid = False
    for number in numbers:
        surrounding_points = matrix.get_number_neighbors(number)
        for point in surrounding_points:
            if point.value != ".":
                number_is_valid = True
                break
            else:
                number_is_valid = False
        if number_is_valid:
            result_sum += int(number.value)

    return result_sum


def main():
    input_file = open("Day3Input.txt")
    input_data = fill_matrix(input_file, get_input_proportions(input_file)["x"], get_input_proportions(input_file)["y"])
    print(solve_part1(input_data, get_numbers(input_data)))


if __name__ == "__main__":
    main()
