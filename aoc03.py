import re

def day03_01(file_path):
    with open(file_path) as f:
        line = ''.join(f.readlines())
        nums_to_calc = re.findall(r"mul\(([0-9]+),([0-9]+)\)", line)

        # print(funcs)

        total = 0
        for pair in nums_to_calc:
            total += int(pair[0]) * int(pair[1])

        print(total)


