class Number:
    def __init__(self, matrix, start, end):
        self.start = start
        self.end = end
        self.len = self.end.x - self.start.x + 1
        if start.coords != end.coords:
            self.points = [start, end]
        else:
            self.points = [start]
        for i in range(end.x - start.x - 1):
            self.points.insert(i + 1, matrix.get_point(start.x + i + 1, start.y))
        self.value = self.get_value()
        self.coords = [i.coords for i in self.points]

    def get_value(self):
        value = ""
        for char in self.points:
            value += char.value
        return value

    def __str__(self):
        return str([self.start.coords, self.end.coords, self.value])
