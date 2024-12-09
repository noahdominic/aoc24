# Advent of Code Day day08_02
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

def day08_01(input_data):
    """
    Solve part 1 of day 08.
    :param input_data: The input data as a string.
    :return: The solution to part 1.
    """
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
                antinode_1, antinode_2 = calculate_antinodes(left_point, right_point)
                antinodes.append(antinode_1)
                antinodes.append(antinode_2)

    lx = len(input_data[0])
    ly = len(input_data)

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

def day08_02(input_data):
    """
    Solve part 2 of day 08.
    :param input_data: The input data as a string.
    :return: The solution to part 2.
    """
    pass
