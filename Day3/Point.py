class Point:
    def __init__(self, x, y, value=""):
        self.x = x
        self.y = y
        if len(value) != 1:
            self.value = ""
        else:
            self.value = value
    def __str__(self):
        return f"{self.x}, {self.y}"
