def day07_01(path):
    with open(path, 'r') as f:
        lines = f.read().splitlines()

        total_calib_result = 0

        for line in lines:
            candidate_result, numbers = line.split(":")
            numbers = numbers.split(" ")[1:]

            numbers_have_valid_combo = has_valid_operation_combo(numbers, candidate_result)

            if numbers_have_valid_combo:
                print(numbers, "is valid!")
                total_calib_result += int(candidate_result)

        print(total_calib_result)



def day07_02(path):
    with open(path, 'r') as f:
        lines = f.read().splitlines()

        print(number_to_boolean_list(1, (2**0)))



def has_valid_operation_combo(numbers, candidate_result):
    possible_combos = 2 ** len(numbers)

    for i in range(possible_combos):
        operations = number_to_boolean_list(i, len(numbers))

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
    possible_combos = 3 ** len(numbers)

    bit_length = (2 ** len(numbers).bit_length())

    for i in range(possible_combos):
        operations = number_to_ternary_list(i, bit_length)

        if 3 in operations:
            print("Currently checking a concatenation")



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
