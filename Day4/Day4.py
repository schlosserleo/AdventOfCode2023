import math


def get_winning_numbers(input_file):
    winning_numbers = []
    input_file.seek(0)
    for line in input_file:
        winning_numbers.append(line[line.find(":") + 1:line.find("|") - 1].split())
    return winning_numbers


def get_numbers_you_have(input_file):
    numbers_you_have = []
    input_file.seek(0)
    for line in input_file:
        numbers_you_have.append(line[line.find("|") + 1:len(line) - 1].split())
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
    return int(result_sum)


def solve_part_2(card_results):
    scratch_cards = [1 for i in range(len(card_results))]
    for index, value in enumerate(len(i) for i in card_results):
        for i in range(value):
            if (index + i + 1) < len(scratch_cards):
                scratch_cards[index + i + 1] += 1 * scratch_cards[index]
    return sum(scratch_cards)


def main():
    input_file = open("Day4Input.txt", "r")
    card_results = get_card_results(get_winning_numbers(input_file), get_numbers_you_have(input_file))
    print(f"Part 1: {solve_part_1(card_results)}\nPart 2: {solve_part_2(card_results)}")


if __name__ == "__main__":
    main()
