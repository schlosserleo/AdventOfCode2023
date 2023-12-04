from Point import *

class Matrix:
    def __init__(self, len_x, len_y, standard_value="."):
        self.len_x = len_x
        self.len_y = len_y
        self.values = [[Point(col, row, standard_value) for col in range(len_y)] for row in range(len_x)]
    def set_point_value(self, x,y, value):
        self.values[y][x] = value
    def get_point_value(self, x, y):
        return self.values[y][x].value
    def create_Point(self, x, y):
        return self.values[y][x]

m = Matrix(5,5)    
P = m.create_Point(3,1)
print(m.get_point_value(3,1))