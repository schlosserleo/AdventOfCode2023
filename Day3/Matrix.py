from Point import *

class Matrix:
        
    def __init__(self, len_x, len_y, standard_value="."):
        self.len_x = len_x
        self.len_y = len_y
        self.matrix = [[Point(col, row, standard_value) for col in range(len_y)] for row in range(len_x)]
        self.values = self.__extract_values() 
        
    def __extract_values(self):
        values = []
        line_str = ""
        for y, line in enumerate(self.matrix):
            for x, point in enumerate(line):
                line_str += point.value
            values.append(line_str)
            line_str = ""
        return values   
        
    def set_value(self, x,y, value):
        self.matrix[y][x].value = value
        self.values[y] = self.values[y][:x] + value + self.values[0][x+1:]
        
    def get_value(self, x, y):
        return self.matrix[y][x].value
    
    def get_point(self, x, y):
        return self.matrix[y][x]
    
    def __str__(self):
        return str(self.values)
        
    def get_number_neighbors(self, number):       #clockwise beginning from letside
        pass
    
    def get_point_neighbors(self, point):
        surrounding_values = []
        
        #left neighbor
        if point.x > 0:
            left_border = False
            
            surrounding_values.append(self.get_point(point.x - 1, point.y))
        else:
            left_border = True
            
        #right neighbor
        if point.x < self.len_x:
            right_border = False
            
            surrounding_values.append(self.get_point(point.x + 1, point.y))
        else:
            right_border = True
        
        #upper neighbors
        if point.y > 0:
            
            upper_border = False
            
            if not left_border:
                surrounding_values.append(self.get_point(point.x -1, point.y - 1))
                
            surrounding_values.append(self.get_point(point.x, point.y -1))
            
            if not right_border:
                surrounding_values.append(self.get_point(point.x + 1, point.y -1))
        else:
            upper_border = True
            
        """
        ...
        .P.
        ...
        """