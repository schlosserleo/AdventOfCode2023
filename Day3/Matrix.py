from Point import *


class Matrix:

    def __init__(self, len_x, len_y, standard_value="."):
        self.len_x = len_x
        self.len_y = len_y
        self.content = [[Point(col, row, standard_value) for col in range(len_y)] for row in range(len_x)]
        self.values = self.__extract_values()

    def __extract_values(self):
        values = []
        line_str = ""
        for y, line in enumerate(self.content):
            for x, point in enumerate(line):
                line_str += point.value
            values.append(line_str)
            line_str = ""
        return values

    def set_value(self, x, y, value, notes=""):
        self.content[y][x].value = value
        self.content[y][x].notes = notes
        self.values[y] = self.values[y][:x] + value + self.values[0][x + 1:]

    def get_value(self, x, y):
        return self.content[y][x].value

    def get_point(self, x, y):
        return self.content[y][x]

    def set_point(self, point):
        self.set_value(point.x, point.y, point.value, point.notes)

    def __str__(self):
        return str(self.values)

    def get_number_neighbors(self, number):
        surrounding_points_of_number = []
        for position in number.points:
            surrounding_points_of_point = self.get_point_neighbors(position)
            for point in surrounding_points_of_point:
                if point not in number.points and point not in surrounding_points_of_number:
                    surrounding_points_of_number.append(point)

        return surrounding_points_of_number

    def get_point_neighbors(self, point):
        surrounding_values = []
        # left neighbor
        if point.x > 0:
            left_border = False
            surrounding_values.append(self.get_point(point.x - 1, point.y))
        else:
            left_border = True
        # right neighbor
        if point.x < self.len_x - 1:
            right_border = False
            surrounding_values.append(self.get_point(point.x + 1, point.y))
        else:
            right_border = True
        # upper neighbors
        if point.y > 0:
            # upper_border = False
            # upper left
            if not left_border:
                surrounding_values.append(self.get_point(point.x - 1, point.y - 1))
            # upper
            surrounding_values.append(self.get_point(point.x, point.y - 1))
            # upper right
            if not right_border:
                surrounding_values.append(self.get_point(point.x + 1, point.y - 1))
        # else:
        # upper_border = True
        # below
        if point.y < self.len_y - 1:
            # below_border = False
            # below left
            if not left_border:
                surrounding_values.append(self.get_point(point.x - 1, point.y + 1))
            # below
            surrounding_values.append(self.get_point(point.x, point.y + 1))
            # below right
            if not right_border:
                surrounding_values.append(self.get_point(point.x + 1, point.y + 1))

        return surrounding_values
