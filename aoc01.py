def day01_01():
    file_path = "input/01.txt"

    with open(file_path) as file:
        file_as_per_line = file.read().splitlines()

        # To know more about this line, see: list comprehension, zip()
        left_list, right_list = zip(*[item.split() for item in file_as_per_line])

        left_list = list(left_list)
        right_list = list(right_list)

        left_list.sort()
        right_list.sort()

        # 1. zip left_list and right_list.
        # 2. form a list out of the tuples created by zipping
        # 3. for each item in the zipped list, calculate the absolute val of the difference
        # 4. use the absolute differences to create new list
        distances = [abs(int(item[0]) - int(item[1])) for item in zip(left_list, right_list)]

        total_distance = sum(distances)

        print(total_distance)

def day01_02():
    file_path = "input/01.txt"
    with open(file_path) as file:
        file_as_per_line = file.read().splitlines()

        # To know more about this line, see: list comprehension, zip()
        left_list, right_list = zip(*[item.split() for item in file_as_per_line])

        counts = {}

        sum = 0

        for item in left_list:
            if not item in counts:
                counts[item] = right_list.count(item)
            sum += int(item) * int(counts[item])

        print(sum) 
