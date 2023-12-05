from Point import *


class Number:
    def __init__(self, matrix, start, end):
        if isinstance(start, Point):
            self.start = start
        else:
            self.start = matrix.get_point(start[0], start[1])
        if isinstance(end, Point):
            self.end = end
        else:
            self.end = matrix.get_point(end[0], end[1])

        self.len = self.end.x - self.start.x + 1

        if self.start.x != self.end.x or self.start.y != self.end.y:
            self.points = [self.start, self.end]
        else:
            self.points = [self.start]

        for i in range(self.end.x - self.start.x - 1):
            self.points.insert(i + 1, matrix.get_point(self.start.x + i + 1, self.start.y))

        self.coords = [point.coords for point in self.points]

        self.value = self.get_value()

    def get_value(self):
        value = ""
        for char in self.points:
            value += char.value
        return value

    def __str__(self):
        return str([self.start.coords, self.end.coords, self.value])
