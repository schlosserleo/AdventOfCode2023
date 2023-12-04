from Point import *

class Number:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.length = self.end.x - self.start.x + 1


    