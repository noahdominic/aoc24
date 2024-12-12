# Advent of Code Day 10



def traverse_map(input_data, x, y, lx, ly, summits=None):
    # Base case: Encounter a '9'
    if input_data[y][x] == 9:
        if summits == None:
            return 1
        elif (x,y) in summits:
            summits.remove((x,y))
            return 1
        else:
            return 0

    # Current value
    current_value = input_data[y][x]

    # Recursively explore all four directions: up, down, left, right
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Down, up, right, left

    total = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy  # Calculate new coordinates
        if 0 <= ny and ny < ly and 0 <= nx and nx < lx:  # Check bounds
            if input_data[ny][nx] == current_value + 1:  # Check condition
                total += traverse_map(input_data, nx, ny, lx, ly, summits)

    return total


def part1(input_data):
    """
    Solve part 1 of day 10.
    :param input_data: The input data as a string.
    :return: The solution to part 1.
    """

    input_data = [[int(x) for x in list(line)] for line in input_data]

    bases = []
    summits = []

    for i, line in enumerate(input_data):
        for j, letter in enumerate(line):
            if letter == 0:
                bases.append((j,i))
            elif letter == 9:
                summits.append((j,i))

    scores = []

    lx = len(input_data[0])
    ly = len(input_data)

    for base in bases:
        scores.append(traverse_map(input_data, base[0], base[1], lx, ly))

    print(f"bases:{bases}\nsummits:{summits}\nscores:{scores}")
    return sum(scores)


def part2(input_data):
    """
    Solve part 2 of day 10.
    :param input_data: The input data as a string.
    :return: The solution to part 2.
    """
    pass
