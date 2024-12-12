import numpy as np
import re

def part1(lines):
    total = 0

    for _ in range(4):
        for line in lines: total += len(re.findall(r"XMAS", line))
        lines = rotate_90deg(lines)

    diagonals_1, diagonals_2 = create_diagonals(lines)

    for line in diagonals_1: total += len(re.findall(r"XMAS", line))
    for line in diagonals_2: total += len(re.findall(r"XMAS", line))

    diagonals_1 = [line[::-1] for line in diagonals_1]
    diagonals_2 = [line[::-1] for line in diagonals_2]

    for line in diagonals_1: total += len(re.findall(r"XMAS", line))
    for line in diagonals_2: total += len(re.findall(r"XMAS", line))

    return total


def part2(lines):
    total = 0
    grid = [list(line) for line in lines]

    padded_grid = [['*' for _ in range(len(grid[0]) + 2)]]
    for row in grid:
        padded_grid += [['*'] + row[::] + ['*']]

    padded_grid += [['*' for _ in range(len(grid[0]) + 2)]]

    for i in range(len(padded_grid)):
        for j in range(len(padded_grid[0])):
            if padded_grid[i][j] == 'A':
                if (padded_grid[i-1][j-1] == 'M' and padded_grid[i+1][j+1] == 'S' or padded_grid[i-1][j-1] == 'S' and padded_grid[i+1][j+1] == 'M') and (padded_grid[i-1][j+1] == 'M' and padded_grid[i+1][j-1] == 'S' or padded_grid[i-1][j+1] == 'S' and padded_grid[i+1][j-1] == 'M'):
                       total += 1

    return total


def rotate_90deg(lines):
    grid = [list(line) for line in lines]
    new_grid = np.transpose(grid)[::-1]
    return [''.join(row).rstrip() for row in new_grid]


def create_diagonals(arr):
    # Convert the array of strings into a 2D numpy array
    arr_2d = np.array([list(row) for row in arr])
    
    # Get the size of the array (rows and columns)
    rows, cols = arr_2d.shape
    
    # List to hold diagonals
    diagonals_1 = []
    diagonals_2 = []
    
    # First set of diagonals (starting from first row)
    for col in range(cols):
        diagonal = []
        r, c = 0, col
        while r < rows and c < cols:
            diagonal.append(arr_2d[r, c])
            r += 1
            c += 1
        diagonals_1.append(''.join(diagonal))
    
    # Second set of diagonals (starting from first column)
    for row in range(1, rows):  # Skip the first row, as it's already covered
        diagonal = []
        r, c = row, 0
        while r < rows and c < cols:
            diagonal.append(arr_2d[r, c])
            r += 1
            c += 1
        diagonals_1.append(''.join(diagonal))
    
    # Now handle diagonals in the reverse direction (starting from first column and top-right corner)
    for col in range(cols - 1, -1, -1):  # Starting from top-right corner
        diagonal = []
        r, c = 0, col
        while r < rows and c >= 0:
            diagonal.append(arr_2d[r, c])
            r += 1
            c -= 1
        diagonals_2.append(''.join(diagonal))
    
    # Second set of diagonals (starting from the first row)
    for row in range(1, rows):  # Skip the first row
        diagonal = []
        r, c = row, cols - 1
        while r < rows and c >= 0:
            diagonal.append(arr_2d[r, c])
            r += 1
            c -= 1
        diagonals_2.append(''.join(diagonal))
    
    return diagonals_1, diagonals_2

