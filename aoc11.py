# Advent of Code Day 11
from functools import cache

@cache
def blinking_algo_recurse(stone, blinks):
    if blinks == 0:
        return 1

    str_stone = str(stone)
    len_stone = len(str_stone)

    if stone == 0:
        return blinking_algo_recurse(1, blinks - 1)
    elif len_stone % 2 == 0:
        return blinking_algo_recurse(int(str_stone[len_stone//2:]), blinks - 1) + blinking_algo_recurse(int(str_stone[:len_stone//2]), blinks - 1)
    else:
        return blinking_algo_recurse(stone * 2024, blinks - 1)


def main_loop(line, blinks):
    return sum([blinking_algo_recurse(stone, blinks) for stone in line])


def part1(input_data):
    """
    Solve part 1 of day 11.
    :param input_data: The input data as a string.
    :return: The solution to part 1.
    """
    lines = [[int(stone) for stone in list(line.split())] for line in input_data]
    BLINKS = 25

    return main_loop(lines[0], BLINKS)


def part2(input_data):
    """
    Solve part 2 of day 11.
    :param input_data: The input data as a string.
    :return: The solution to part 2.
    """
    lines = [[int(stone) for stone in list(line.split())] for line in input_data]
    BLINKS = 75

    return main_loop(lines[0], BLINKS)

