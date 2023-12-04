INPUT_FILE = open("Day2/Day2Input.txt")

def parse_line(line):
    double_point_position = line.find(":") 
    cleared_line = line[double_point_position + 2:]
    game_number = int(line[5 : double_point_position])
    
    sets = []
    set_content = {"red" : 0, "blue" : 0, "green" : 0}
    color = ""
    
    color_count_str = ""
    previous_was_digit = False
    
    for index, value in enumerate(cleared_line):
        if value.isdigit():
            color_count_str += value
            previous_was_digit = True
        elif value == " " and previous_was_digit:
            color_count = int(color_count_str)
            previous_was_digit = False
        elif value.isalpha():
            color += value
        elif value == ",":
            set_content[color] = color_count
            color_count_str = ""
            color = ""
        if value == ";" or index == len(cleared_line)-1:
            set_content[color] = color_count
            sets.append(set_content)
            set_content = {"red" : 0, "blue" : 0, "green" : 0}
            color_count_str = ""
            color = ""
    
    return [game_number, sets]

def solve_part1():
    red_max = 12
    blue_max = 14
    green_max = 13
    sum_of_game_numbers = 0
    for line in INPUT_FILE:
        parsed_line = parse_line(line)
        for set in parsed_line[1]:
            if set["red"] <= red_max and set["blue"] <= blue_max and set["green"] <= green_max:
                set_is_valid = True
            else:
                set_is_valid = False
                break
        if set_is_valid:
            sum_of_game_numbers += parsed_line[0]
    INPUT_FILE.seek(0)
    return sum_of_game_numbers

def solve_part2():
    red_min = 100
    blue_min = 100
    green_min = 100
    sum_of_powers = 0
    for line in INPUT_FILE:
        parsed_line = parse_line(line)
        for set in parsed_line[1]:
            if set["red"] < red_min and set["red"] != 0:
                red_min = set["red"]
            if set["blue"] < blue_min and set[""]:
                blue_min = set["blue"]
            if set["green"] < green_min:
                green_min = set["green"]
        set_power = red_min * blue_min * green_min
        sum_of_powers += set_power
        
    return sum_of_powers
print("Part 1 :" + str(solve_part1())+"\nPart 2 :" + str(solve_part2())) 