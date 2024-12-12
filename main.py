import sys
import importlib

def main ():
    # Default values
    day = 0
    part = 0
    test = True

    for arg in sys.argv[1:]:
        arg_parsed = arg.split('=')
        match arg_parsed[0]:
            case 'day':
                day = int(arg_parsed[1])
            case 'part':
                part = int(arg_parsed[1])
            case 'final':
                test = False
            case _:
                pass

    file_path = f"input/{day:02d}{'-test' if test else ''}.txt"

    try:
        wanted_module = importlib.import_module(f"aoc{day:02d}")
    except ModuleNotFoundError:
        raise ValueError(f"Module for day {day:02d} not found!")

    wanted_function = wanted_module.part2 if part == 2 else wanted_module.part1

    with open(file_path, 'r') as f:
    # with open('input/10-test.txt', 'r') as f:
        lines = f.read().splitlines()
        print(lines)

        print(wanted_function(lines))

if __name__ == "__main__":
    main()
