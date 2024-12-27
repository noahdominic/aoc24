# Advent of Code Day 13
import numpy as np


def calculate_solution(s, t, u, v, w, x, a, b):
    """
    This function calculates solution using the determinant/matrix method
    by vieweing the two numbers as a system of equation:
        as + bt = u
        av + bw = x
    where a is the number of times buttom A is pressed,
    b is the number of times button B is pressed,
    s is the x contribution of a press of button A,
    t is the x contribution of a press of button B,
    u is the total contributions needed for x,
    v is the y contribution of a press of button A,
    w is the y contribution of a press of button B,
    and x is the total contributions eneded for y.
    """

    A = np.array([[s, t], [v, w]])
    C = np.array([u, x])

    det_A = np.linalg.det(A)
    if det_A != 0:
        solution = np.linalg.solve(A, C)
        a, b = solution[0], solution[1]
    else:
        a, b = None, None

    a = round(a, 3)
    b = round(b, 3)

    a = int(a) if a.is_integer() else None
    b = int(b) if b.is_integer() else None

    return a, b

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
            s, t, u, v, w, x = 0, 0, 0, 0, 0, 0
            if a is not None and b is not None:
                print(f"Solution is possible! a={a}, b={b}")
                cost = 3 * a + b
                print(f"cost={cost}")
                total_cost += cost
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

        print(s, t, u, v, w, x)

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
            s, t, u, v, w, x = 0, 0, 0, 0, 0, 0
            if a is not None and b is not None:
                print(f"Solution is possible! a={a}, b={b}")
                cost = 3 * a + b
                print(f"cost={cost}")
                total_cost += cost
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

        print(s, t, u, v, w, x)

    return total_cost
