# Advent of Code Day 13
def part1(input_data):
    """
    Solve part 1 of day 13.
    :param input_data: The input data as a string.
    :return: The solution to part 1.
    """

    s = 0
    t = 0
    u = 0
    v = 0
    w = 0
    x = 0
    a = 0
    b = 0
    total_cost = 0
    for line in input_data:
        # In my analysis, I've named the variables as such:
        # s = A's x
        # t = B's x
        # u = needed x
        # v = A's y
        # w = B's y
        # x = needed y
        # a = (to be calculated) times A is pressed
        # b = (to  be calculated) times B is pressed

        if line == '':
            a, b = calculate_solution(s, t, u, v, w, x, a, b)
            b = (s*x - u*v)/(s*w - t*v)
            a = (u - b*t)/s
            print(f"a={a}, b={b}")
            if a.is_integer() and b.is_integer():
                total_cost += 3 * a + b
            s, t, u, v, w, x = 0, 0, 0, 0, 0, 0
            continue

        label, numbers = line.split(':')
        if label == 'Prize':
            items = numbers.split(',')
            u = int(items[0].split('=')[1])
            x = int(items[1].split('=')[1])
        elif label == 'Button A':
            items = numbers.split(',')
            s = int(items[0].split('+')[1])
            v = int(items[1].split('+')[1])
        elif label == 'Button B':
            items = numbers.split(',')
            t = int(items[0].split('+')[1])
            w = int(items[1].split('+')[1])
        else:
            pass

    return total_cost

def part2(input_data):
    """
    Solve part 2 of day 13.
    :param input_data: The input data as a string.
    :return: The solution to part 2.
    """
    s = 0
    t = 0
    u = 0
    v = 0
    w = 0
    x = 0
    a = 0
    b = 0
    total_cost = 0
    for line in input_data:
        # In my analysis, I've named the variables as such:
        # s = A's x
        # t = B's x
        # u = needed x
        # v = A's y
        # w = B's y
        # x = needed y
        # a = (to be calculated) times A is pressed
        # b = (to  be calculated) times B is pressed

        if line == '':
            a, b = calculate_solution(s, t, u, v, w, x, a, b)
            b = (s*x - u*v)/(s*w - t*v)
            a = (u - b*t)/s
            print(f"a={a}, b={b}")
            if a.is_integer() and b.is_integer():
                total_cost += 3 * a + b
            s, t, u, v, w, x = 0, 0, 0, 0, 0, 0
            continue
        label, numbers = line.split(':')
        if label == 'Prize':
            items = numbers.split(',')
            u = 10000000000000 + int(items[0].split('=')[1])
            x = 10000000000000 + int(items[1].split('=')[1])
        elif label == 'Button A':
            items = numbers.split(',')
            s = int(items[0].split('+')[1])
            v = int(items[1].split('+')[1])
        elif label == 'Button B':
            items = numbers.split(',')
            t = int(items[0].split('+')[1])
            w = int(items[1].split('+')[1])
        else:
            pass

    return total_cost
