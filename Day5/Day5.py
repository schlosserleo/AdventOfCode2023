from tqdm import tqdm


def convert_input_file(input_file):
    return [line for line in input_file]


def get_seeds(almanac):
    return [int(seed) for seed in almanac[0][6:].split()]


def get_translation_maps(almanac):
    translation_maps = []
    temp_map = []
    count = 0
    for line in almanac[3:]:
        if line != "\n" and line[0].isdigit():
            temp_map.append([int(i) for i in line.split()])
            count += 1
        else:
            if temp_map:
                translation_maps.append(temp_map)
            temp_map = []
    translation_maps.append(temp_map)
    return translation_maps


def solve_part_1(almanac):
    seeds = get_seeds(almanac)
    translation_maps = get_translation_maps(almanac)
    smallest_num = 100000000000000
    for seed in seeds:
        for translation_map in translation_maps:
            for line in translation_map:
                if line[1] <= seed < (line[1] + line[2]):
                    seed += (line[0] - line[1])
                    break
        if seed < smallest_num:
            smallest_num = seed
    return smallest_num


def solve_part_2(translation_maps, almanac):
    part_1_seeds = get_seeds(almanac)
    smallest_num = 1000000000000000000
    with tqdm(total=132561557373) as pbar:
        for index, part_1_seed in enumerate(part_1_seeds):
            if index % 2 == 0:
                for seed in range(part_1_seed, part_1_seed + part_1_seeds[index + 1]):
                    for translation_map in translation_maps:
                        for line in translation_map:
                            if line[1] <= seed < (line[1] + line[2]):
                                seed += (line[0] - line[1])
                                break
                        pbar.update(1)
                    if seed < smallest_num:
                        smallest_num = seed
    return smallest_num


def main():
    input_file = open("Day5Input.txt", "r")
    almanac = convert_input_file(input_file)
    translation_maps = get_translation_maps(almanac)
    input_file.close()
    print(f"Part 1: {solve_part_1(almanac)}")
    print(f"Part 2: {solve_part_2(translation_maps, almanac)}")


if __name__ == "__main__":
    main()
