import math


def get_winning_numbers(input_file):
    winning_numbers = []
    input_file.seek(0)
    for line in input_file:
        winning_numbers.append(line[10:39].split())
    return winning_numbers


def get_numbers_you_have(input_file):
    numbers_you_have = []
    input_file.seek(0)
    for line in input_file:
        numbers_you_have.append(line[42:116].split())
    return numbers_you_have


def get_card_results(winning_numbers, numbers_you_have):
    card_results = []
    matched_numbers = []
    for card_num, numbers in enumerate(winning_numbers):
        for number in numbers:
            if number in numbers_you_have[card_num]:
                matched_numbers.append(number)
        card_results.append(matched_numbers)
        matched_numbers = []
    return card_results


def solve_part_1(card_results):
    result_sum = 0
    for matched_numbers in card_results:
        if len(matched_numbers) != 0:
            result_sum += math.pow(2, len(matched_numbers) - 1)
    return result_sum


def main():
    input_file = open("Day4Input.txt", "r")
    card_results = get_card_results(get_winning_numbers(input_file), get_numbers_you_have(input_file))
    print(f"Part 1: {solve_part_1(card_results)}")


if __name__ == "__main__":
    main()
