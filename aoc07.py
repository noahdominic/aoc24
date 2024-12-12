def part1(lines):
    return day07(lines, has_valid_operation_combo)



def part2(lines):
    return day07(lines, has_valid_operation_combo_2)



def day07(lines, validator):
    total_calib_result = 0

    for line in lines:
        candidate_result, numbers = line.split(":")
        numbers = numbers.split(" ")[1:]

        numbers_have_valid_combo = validator(numbers, candidate_result)

        if numbers_have_valid_combo:
            total_calib_result += int(candidate_result)

    return total_calib_result



def perform_concatenation(numbers, operations):
    new_numbers = []

    concat_buffer = numbers [0]

    for i, number in enumerate(numbers[1:]):
        if operations[i] == 2:
            concat_buffer += number
        else:
            new_numbers.append(concat_buffer)
            concat_buffer = number

    if not concat_buffer == "":
        new_numbers.append(concat_buffer)

    return new_numbers, [i for i in operations if i != 2]




def has_valid_operation_combo(numbers, candidate_result):
    possible_combos = 2 ** (len(numbers) - 1)

    for i in range(possible_combos):
        operations = number_to_boolean_list(i, len(numbers)-1)

        accumulator = int(numbers[0])

        for next_number, operation in zip(numbers[1:], operations):
            if operation: # That is, if the current operation is True,
                accumulator += int(next_number)
            else:
                accumulator *= int(next_number)

        if accumulator == int(candidate_result):
            return True
    return False



def has_valid_operation_combo_2(numbers, candidate_result):
    possible_combos = 3 ** (len(numbers) - 1)

    for i in range(possible_combos):
        operations = number_to_ternary_list(i, len(numbers) - 1)

        accumulator = int(numbers[0])

        for next_number, operation in zip(numbers[1:], operations):
            if operation == 1:
                accumulator += int(next_number)
            elif operation == 0:
                accumulator *= int(next_number)
            else:
                accumulator = int(str(accumulator) + next_number)

        if accumulator == int(candidate_result):
            return True


    return False



def number_to_boolean_list(number, bit_length):
    boolean_list = []
    for _ in range(bit_length):
        # extract the least significant bit and add to the list
        boolean_list.append(bool(number & 1))
        # right-shift the number
        number >>= 1
    return boolean_list



def number_to_ternary_list(number, digit_length):
    ternary_list = []
    for _ in range(digit_length):
        # extract the least significant ternary digit and add to the list
        ternary_list.append(number % 3)
        # divide the number by 3 to move to the next ternary digit
        number //= 3
    return ternary_list
