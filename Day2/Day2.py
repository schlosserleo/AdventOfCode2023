INPUT_FILE = open("Day2Input.txt")


def parse_line(line):
    double_point_position = line.find(":")
    cleared_line = line[double_point_position + 2:]
    game_number = int(line[5: double_point_position])

    sets = []
    set_content = {"red": 0, "blue": 0, "green": 0}
    color = ""
    color_count = 0
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
        if value == ";" or index == len(cleared_line) - 1:
            set_content[color] = color_count
            sets.append(set_content)
            set_content = {"red": 0, "blue": 0, "green": 0}
            color_count_str = ""
            color = ""

    return [game_number, sets]


def solve_part1():
    red_max = 12
    blue_max = 14
    green_max = 13
    sum_of_game_numbers = 0
    subset_is_valid = False
    for line in INPUT_FILE:
        parsed_line = parse_line(line)
        for subset in parsed_line[1]:
            if subset["red"] <= red_max and subset["blue"] <= blue_max and subset["green"] <= green_max:
                subset_is_valid = True
            else:
                subset_is_valid = False
                break
        if subset_is_valid:
            sum_of_game_numbers += parsed_line[0]
    INPUT_FILE.seek(0)
    return sum_of_game_numbers


def solve_part2():
    red_min = 0
    blue_min = 0
    green_min = 0
    sum_of_powers = 0
    for line in INPUT_FILE:
        parsed_line = parse_line(line)
        for subset in parsed_line[1]:
            if subset["red"] > red_min:  # and set["red"] != 0:
                red_min = subset["red"]
            if subset["blue"] > blue_min:  # and set["blue"] != 0:
                blue_min = subset["blue"]
            if subset["green"] > green_min:  # and set["green"] != 0:
                green_min = subset["green"]
        set_power = red_min * blue_min * green_min
        sum_of_powers += set_power
        red_min = 0
        blue_min = 0
        green_min = 0

    return sum_of_powers


def main():
    print(f"Part 1: {solve_part1()}\nPart 2: {solve_part2()}")


if __name__ == "__main__":
    main()
