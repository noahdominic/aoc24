from aoc00 import greet
# from aoc01 import day01_01, day01_02
# from aoc02 import day02_01, day02_02
# from aoc03 import day03_01, day03_02
# from aoc04 import day04_01, day04_02
# from aoc05 import day05_01, day05_02
# from aoc06 import day06_01# , day05_02
# from aoc07 import day07_01, day07_02
import aoc09

def main ():
    greet("Charlie")
    # day01_01()
    # day01_02()
    # day02_01("input/02.txt")
    # day02_02("input/02.txt")
    # day03_01("input/03.txt")
    # day03_02("input/03.txt")
    # day04_01("input/04.txt")
    # day04_02("input/04.txt")
    # day05_01("input/05.txt")
    # day05_02("input/05.txt")
    # day06_01("input/06.txt")
    # day07_01("input/07.txt")
    # day07_02("input/07.txt")

    with open('input/09.txt', 'r') as f:
        lines = f.read().splitlines()
        print(lines)

        print(aoc09.day09_02(lines))

if __name__ == "__main__":
    main()
