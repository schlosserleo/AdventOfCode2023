# def create_matrix():
#     INPUT_FILE = open("Day3/Day3Input.txt")
#     matrix = []

#     for line in INPUT_FILE:
#         matrix.append(line.strip())
        
#     return matrix

# MATRIX = create_matrix()
    
MATRIX = ["upperupper",
          "left123right",
          "belowbelow"]

number_coord_start = [4,1]
number_coord_end = [6,1]

def get_sorrounding_symbols(number_coord_start, number_coord_end):              #number_start: [<Zeile(index in MATRIX)>, <Spalte(index in Zeile)>]
    left_number_coordinates = [number_start[0],number_start[1] - 1]
    print(left_number_index)
    # right_number_index =
    # over_number = ""
    # under_number = ""
    
def get_coordinates_of_number_surroundings(number_coord_x_start, number_coord_x_end, position):
    if position == "left":
        return [number_coord_x_start[1], number_coord_x_start[0] - 1]
    elif position == "right":
        return [number_coord_x_end[1], number_coord_x_end[0] + 1]
    elif position == "upper":
        return [[number_coord_x_start[1] - 1, number_coord_x_start[0] - 1], [number_coord_x_end[1] - 1, number_coord_x_end[0] + 1]]
    elif position == "below":
        return [[number_coord_x_start[1] + 1, number_coord_x_start[0] - 1], [number_coord_x_end[1] + 1, number_coord_x_end[0] + 1]]

def parse_matrix(coords):
    y = coords[0]
    x = coords[1]
    return MATRIX[y][x]
    
print(parse_matrix(get_coordinates_of_number_surroundings(number_coord_start, number_coord_end, "left")))
    
    