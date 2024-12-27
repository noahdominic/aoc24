# Advent of Code Day 12

from collections import defaultdict


def traverse_map(grid, x, y, lx, ly, logged, expected, perimeter_log=None):
    """
    Traverse a grid recursively, marking nodes with the expected symbol.

    :param grid: 2D list representing the grid.
    :param x: Current x-coordinate (row).
    :param y: Current y-coordinate (column).
    :param lx: Number of rows in the grid.
    :param ly: Number of columns in the grid.
    :param logged: Set to keep track of visited nodes.
    :param expected: Symbol expected for traversal.
    """
    # Check if (x, y) is out of bounds or already visited; Not visited over all but visited during THIS traversal
    # Like, this point might have already been visited when traversing region `A` but right now, we're
    # traversing region `B` so this point should NOT be in `logged`.  The handling of the logic is in main func.
    if (x, y) in logged:
        return 0

    # Check if the current cell matches the expected symbol
    if x < 0 or y < 0 or x >= lx or y >= ly or grid[y][x] != expected:
        if perimeter_log is not None:
            perimeter_log.add((x,y))
        return 1  # Non-part neighbor contributes to the perimeter

    # Mark the current node as visited
    logged.add((x, y))

    # Explore neighboring cells in four directions (up, down, left, right)
    perimeter = 0
    perimeter += traverse_map(grid, x - 1, y, lx, ly, logged, expected, perimeter_log)  # Up
    perimeter += traverse_map(grid, x + 1, y, lx, ly, logged, expected, perimeter_log)  # Down
    perimeter += traverse_map(grid, x, y - 1, lx, ly, logged, expected, perimeter_log)  # Left
    perimeter += traverse_map(grid, x, y + 1, lx, ly, logged, expected, perimeter_log)  # Right

    return perimeter


def part1(input_data):
    """
    Solve part 1 of day 12.
    :param input_data: The input data as a string.
    :return: The solution to part 1.
    """
    logged = set()
    total = 0
    ly = len(input_data)
    lx = len(input_data[0])
    for y, line in enumerate(input_data):
        for x, letter in enumerate(line):
            if (x, y) not in logged:
                temp_logged = set()
                perimeter = traverse_map(input_data, x, y, lx, ly, temp_logged, letter)
                area = len(temp_logged)
                total += perimeter * area
                logged |= temp_logged

    return total



def count_straight_lines(coordinates):
    # Group points by x-coordinates for vertical lines and y-coordinates for horizontal lines
    vertical_groups = defaultdict(list)
    horizontal_groups = defaultdict(list)
    
    for x, y in coordinates:
        vertical_groups[x].append(y)  # Group y-coordinates by x
        horizontal_groups[y].append(x)  # Group x-coordinates by y
    
    def count_consecutive_lines(groups):
        line_count = 0
        for key, points in groups.items():
            points.sort()  # Sort to check consecutive points
            # Count consecutive pairs
            line_count += sum(1 for i in range(len(points) - 1) if points[i + 1] - points[i] == 1)
        return line_count
    
    # Count vertical and horizontal lines
    vertical_lines = count_consecutive_lines(vertical_groups)
    horizontal_lines = count_consecutive_lines(horizontal_groups)
    
    return vertical_lines + horizontal_lines


def part2(input_data):
    """
    Solve part 2 of day 12.
    :param input_data: The input data as a string.
:return: The solution to part 2.
    """
    logged = set()
    total = 0
    ly = len(input_data)
    lx = len(input_data[0])
    for y, line in enumerate(input_data):
        for x, letter in enumerate(line):
            if (x, y) not in logged:
                temp_logged = set()
                perimeter_log = set()
                _ = traverse_map(input_data, x, y, lx, ly, temp_logged, letter, perimeter_log)
                area = len(temp_logged)
                print(letter , ":", perimeter_log)
                print(count_straight_lines(perimeter_log))
                # print(area, count_straight_lines(perimeter_log))
                # total += count_straight_lines(perimeter_log) * area
                logged |= temp_logged

    return total
