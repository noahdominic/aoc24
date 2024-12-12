# Advent of Code Day part2
def calculate_antinodes(point_a, point_b):
    """
    Calculate the coordinates of the two antinodes given two points as tuples (x1, y1) and (x2, y2).

    :param point_a: Tuple representing point A (x1, y1)
    :param point_b: Tuple representing point B (x2, y2)
    :return: Tuples representing the coordinates of Antinode_A and Antinode_B
    """
    # Unpack the tuples
    x1, y1 = point_a
    x2, y2 = point_b

    # Vector from A to B
    dx = x2 - x1
    dy = y2 - y1

    # Antinode_A is twice as far from A in the direction of B
    antinode_a = (x1 + 2 * dx, y1 + 2 * dy)

    # Antinode_B is twice as far from B in the direction opposite to A
    antinode_b = (x2 - 2 * dx, y2 - 2 * dy)

    return antinode_a, antinode_b

def calculate_resonant_antinodes(point_a, point_b, lx, ly):
    """
    Calculate the coordinates of theoretically-infinite antinodes given two points as tupes (x1, y1) and (x2, y2), max x coordinate lx, and max y coordinate ly.

    :param point_a: Tuple representing point A (x1, y1)
    :param point_b: Tuple representing point B (x2, y2)
    :param lx: Horizontal bounds of grid
    :param ly: Vertical bounds of grid
    :return: List of tuples representing the coordinates of all antinodes
    """

    x1, y1 = point_a
    x2, y2 = point_b

    dx = x2 - x1
    dy = y2 - y1

    def is_within_bounds(x, y):
        return x >= 0 and x < lx and y >= 0 and y < ly

    antinodes = []

    # calculate resonances of what was Antinode A
    multiplier = 1
    while True:
        candidate_antinode = (x1 + multiplier * dx, y1 + multiplier * dy)

        if not is_within_bounds(candidate_antinode[0], candidate_antinode[1]):
            break

        antinodes.append(candidate_antinode)

        multiplier += 1

    # calculate resonances of what was Antinode B
    multiplier = 1
    while True:
        candidate_antinode = (x2 - multiplier * dx, y2 - multiplier * dy)

        if not is_within_bounds(candidate_antinode[0], candidate_antinode[1]):
            break

        antinodes.append(candidate_antinode)

        multiplier += 1

    return antinodes

def part1(input_data):
    """
    Solve part 1 of day 08.
    :param input_data: The input data as a string.
    :return: The solution to part 1.
    """
    antenna = {}
    lx = len(input_data[0])
    ly = len(input_data)


    # Extract all positions of antennas
    for y, line in enumerate(input_data):
        for x, char in enumerate(line):
            if char != '.':
                if char not in antenna:
                    antenna[char] = [(x, y)]
                else:
                    antenna[char].append((x, y))

    # Calculate positions of antinodes
    antinodes = []
    for key, points in antenna.items():
        for i, left_point in enumerate(points[:len(points) - 1]):
            for right_point in points[i+1:]:
                antinode_1, antinode_2 = calculate_antinodes(left_point, right_point)
                antinodes.append(antinode_1)
                antinodes.append(antinode_2)


    antinodes = set(antinodes)  # Remove duplicates
    antinodes = list(           # Remove out of bounds
            filter(
                lambda point:
                    point[0] < lx
                    and point[0] >= 0
                    and point[1] < ly
                    and point[1] >= 0,
            antinodes))

    return len(antinodes)

def part2(input_data):
    """
    Solve part 2 of day 08.
    :param input_data: The input data as a string.
    :return: The solution to part 2.
    """

    lx = len(input_data[0])
    ly = len(input_data)

    antenna = {}

    # Extract all positions of antennas
    for y, line in enumerate(input_data):
        for x, char in enumerate(line):
            if char != '.':
                if char not in antenna:
                    antenna[char] = [(x, y)]
                else:
                    antenna[char].append((x, y))

    # Calculate positions of antinodes
    antinodes = []
    for key, points in antenna.items():
        for i, left_point in enumerate(points[:len(points) - 1]):
            for right_point in points[i+1:]:
                possible_antinodes = calculate_resonant_antinodes(left_point, right_point, lx, ly)
                antinodes += possible_antinodes

    antinodes = set(antinodes)  # Remove duplicates
    antinodes = list(           # Remove out of bounds
            filter(
                lambda point:
                    point[0] < lx
                    and point[0] >= 0
                    and point[1] < ly
                    and point[1] >= 0,
            antinodes))

    return len(antinodes)
