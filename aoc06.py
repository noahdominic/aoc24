UP, RIGHT, DOWN, LEFT = range(4)

def day06_01(file_path):
    with open(file_path, 'r') as f:
        grid = [list(line) for line in f.read().splitlines()]

        print(grid)
        x = 0
        y = 0

        guard_glyphs = ['^', '>', 'v', '<']

        direction = UP

        lx = len(grid[0])
        ly = len(grid)
        for i in range(ly):
            for j in range(lx):
                if grid[i][j] in guard_glyphs:
                    x = j
                    y = i
                    direction = guard_glyphs.index(grid[i][j])

        print(direction, x, y)

        while True:
            grid[y][x] = 'X'
            possible_x, possible_y = next_pos(x, y, direction)
            if possible_x < 0 or possible_x >= lx or possible_y < 0 or possible_y >= ly:
                break;
            if (grid[possible_y][possible_x] == '#'):
                direction = (direction + 1) % 4
                continue
            x, y = (possible_x, possible_y)

        for line in grid:
            print(line)

        print(f"TOTAL: {sum(row.count('X') for row in grid)}")



def next_pos(x, y, direction):
    if direction == UP:
        return (x, y - 1)
    elif direction == RIGHT:
        return (x + 1, y)
    elif direction == DOWN:
        return (x, y + 1)
    elif direction == LEFT:
        return (x - 1, y)
    else:
        raise ValueError("Invalid glyph direction")
