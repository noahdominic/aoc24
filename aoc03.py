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

def day03_02(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        command_matches = re.finditer(r"do\(\)|don't\(\)", lines[0])
        num_matches = re.finditer(r"mul\(([0-9]+),([0-9]+)\)", lines[0])

        commands = [{"type": "command", "content": match.group(0), "position": match.span()[0]} for match in command_matches]
        numbers = [
            {"type": "number_pair", "content": (int(match.group(1)), int(match.group(2))), "position": match.span()[0]}
                for match in num_matches
        ]

        merged_list = sorted(commands + numbers, key=lambda x: x["position"])

        active = True
        total = 0

        for item in merged_list:
            if item["type"] == "command":
                active = item["content"] == "do()"
            elif item["type"] == "number_pair" and active:
                total += item["content"][0] * item["content"][1]

        print(total)

