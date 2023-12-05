class Point:
    def __init__(self, x, y, value="", number=None):
        self.x = x
        self.y = y
        if len(value) != 1:
            self.value = ""
        else:
            self.value = value
        self.coords = [self.x, self.y]
        self.number = number

    def __str__(self):
        return f"{self.x}, {self.y}"

    def get_list(self):
        return [[self.x, self.y], self.value]

    def get_value(self):
        return f"{self.value}"
