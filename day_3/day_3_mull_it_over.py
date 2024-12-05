import re

test_memory = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
test_memory_with_do_donts = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""

def attempt_to_execute_mul_program(memory):
    input_numbers_to_valid_mul_instructions = re.findall(r'mul\((\d*),(\d*)\)', memory)

    return sum(
        [int(first_number_as_string) * int(second_number_as_string) for (first_number_as_string, second_number_as_string) in input_numbers_to_valid_mul_instructions]
    )

def attempt_to_execute_mul_program_version_do_donts(memory):
    """
    the following example shows that we should only pick the 'most recent' "don't()" once we find a "do()"
    >>> attempt_to_execute_mul_program_version_do_donts(r"aaadon't()xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")
    48

    In my view, the text "Only the most recent do() or don't() instruction applies." implies that
    the solution to the following is 35, since after hitting the 'do()' block just before mul(1,7)
    we should only 
    >>> attempt_to_execute_mul_program_version_do_donts(r"don't()mul(1,3)don't()mul(1,5)do()mul(1,7)do()")
    7
    """
    # step through the memory left to right, find either a mul, a do, a don't, put into capture groups
    regex_either_valid_mul_do_or_dont = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"

    total_so_far = 0
    inside_dont_do_block = False

    for (mul_number_1, mul_number_2, do_token, dont_token) in re.findall(regex_either_valid_mul_do_or_dont, memory):
        # print((mul_number_1, mul_number_2, do_token, dont_token))
        if mul_number_1 and not inside_dont_do_block:
            total_so_far += int(mul_number_1) * int(mul_number_2)
        elif dont_token:
            inside_dont_do_block = True
        elif do_token:
            inside_dont_do_block = False

    return total_so_far

if __name__ == "__main__":
    actual_memory_data = open('day_3_raw_data.txt').read()
    # print(actual_memory_data)
    # print(attempt_to_execute_mul_program_version_do_donts(actual_memory_data))
    # test_case = r"don't()mul(1,3)do()mul(1,4)don't()mul(1,5)don't()mul(1,2)do()"
    test_case = test_memory
    print(attempt_to_execute_mul_program_version_do_donts(actual_memory_data))
    pass