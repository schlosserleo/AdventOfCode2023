from Matrix import *
from Number import *


def get_matrix_dimension(input_file):
    input_file.seek(0)
    input_as_list = []
    for line in input_file:
        input_as_list.append(line.strip())

    return {"x": len(input_as_list[0]), "y": len(input_as_list)}


def fill_matrix(content, len_x, len_y):
    matrix = Matrix(len_x, len_y)
    content.seek(0)
    for y, line in enumerate(content):
        for x, char in enumerate(line.strip()):
            matrix.set_value(x, y, char)

    return matrix


def get_numbers(matrix):
    numbers = []
    is_building_number = False
    number_start = matrix.get_point(0, 0)
    prev_point = matrix.get_point(0, 0)

    for line in matrix.content:
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


def solve_part_1(matrix, numbers):
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


def add_number_to_digit_points(matrix, numbers):
    for number in numbers:
        for point in number.points:
            point.number = number
            matrix.set_point(point)


def convert_matrix_for_part_2(matrix):
    add_number_to_digit_points(matrix, get_numbers(matrix))


def solve_part_2(matrix):
    result_sum = 0
    for line in matrix.content:
        for point in line:
            if point.value == "*":
                neighbour_numbers = []
                for neighbour in matrix.get_point_neighbors(point):
                    if neighbour.value.isdigit():
                        if neighbour.number.coords not in [i.number.coords for i in neighbour_numbers]:
                            neighbour_numbers.append(neighbour)
                if len(neighbour_numbers) == 2:
                    result_sum += int(neighbour_numbers[0].number.value) * int(neighbour_numbers[1].number.value)
    return result_sum


def main():
    input_file = open("Day3Input.txt")
    matrix = fill_matrix(input_file, get_matrix_dimension(input_file)["x"], get_matrix_dimension(input_file)["y"])
    print(f"Part 1:{solve_part_1(matrix, get_numbers(matrix))}")
    convert_matrix_for_part_2(matrix)
    print(f"Part 2:{solve_part_2(matrix)}")


if __name__ == "__main__":
    main()
