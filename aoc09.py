# Advent of Code Day 09
from itertools import zip_longest



def pop_rightmost_number(mixed_list):
    for i in range(len(mixed_list) - 1, -1, -1):  # Traverse list from the end
        if isinstance(mixed_list[i], (int, float)):  # Check if the item is a number
            return mixed_list.pop(i)  # Remove and return the number
    return None



def day09_01(input_data):
    """
    Solve part 1 of day 09.
    :param input_data: The input data as a string.
    :return: The solution to part 1.
    """
    checksum = 0

    data = input_data[0]

    numbers = data[::2]
    gaps = data[1::2]

    decoded = []
    reverse_decoded = []
    for i, (number, gap) in enumerate(zip_longest(numbers, gaps, fillvalue='0')):
        decoded += [i] * int(number) + ['.'] * int(gap)

    for i in range(sum([int(x) for x in numbers])):
        if i >= len(decoded):
            break
        if decoded[i] == '.':
            decoded[i] = pop_rightmost_number(decoded)

    decoded = [num for num in decoded if isinstance(num,int) ]

    return sum([ i * num for i, num in enumerate(decoded)])



def day09_02(input_data):
    """
    Solve part 2 of day 09.
    :param input_data: The input data as a string.
    :return: The solution to part 2.
    """
    pass
