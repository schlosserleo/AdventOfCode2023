def convert_input_file(input_file):
    return [line for line in input_file]


def get_seeds_part_1(almanac):
    return [int(seed) for seed in almanac[0][6:].split()]


def get_seeds_part_2(almanac):
    part_1_seeds = get_seeds_part_1(almanac)
    part_2_seeds = []
    for index, seed in enumerate(part_1_seeds):
        if index % 2 == 0:
            part_2_seeds += [i for i in range(seed, seed + part_1_seeds[index + 1])]
    return part_2_seeds


def get_translation_maps(almanac):
    translation_maps = []
    temp_map = []
    for line in almanac[3:]:
        if line != "\n" and line[0].isdigit():
            temp_map.append([int(i) for i in line.split()])
        else:
            if temp_map:
                translation_maps.append(temp_map)
            temp_map = []
    translation_maps.append(temp_map)
    return translation_maps


def get_location(translation_maps, seed):
    temp_num = seed
    for translation_map in translation_maps:
        for line in translation_map:
            if line[1] <= temp_num < (line[1] + line[2]):
                temp_num += (line[0] - line[1])
                break
    return temp_num


def solve_part_1(almanac):
    locations = []
    for seed in get_seeds_part_1(almanac):
        locations.append(get_location(get_translation_maps(almanac), seed))
    return min(locations)


def solve_part_2(almanac):
    locations = []
    for seed in get_seeds_part_2(almanac):
        locations.append(get_location(get_translation_maps(almanac), seed))
    return min(locations)


def main():
    input_file = open("Day5Input.txt", "r")
    almanac = convert_input_file(input_file)
    print(f"Part 1: {solve_part_1(almanac)}\nPart 2: {solve_part_2(almanac)}")


if __name__ == "__main__":
    main()
