import aocd

test_report_data = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
]

def parse_raw_csv_data(raw_data_string):
    return [list(map(int, line.split())) for line in raw_data_string.split("\n")]

def report_is_safe(report):
    """
    >>> report_is_safe([7, 6, 4, 2, 1])
    True

    >>> report_is_safe([1, 2, 7, 8, 9])
    False
    """
    if len(report) < 2:
        return True
    
    first_pair_is_increasing = (report[0] < report[1])
    
    for (level, next_level) in zip(report, report[1:]):
        this_pair_is_increasing = (level < next_level)
        if (first_pair_is_increasing != this_pair_is_increasing) or not (1 <= abs(next_level - level) <= 3):
            return False
        
    return True

def report_is_safe_dampener_version(report):
    """
    >>> report_is_safe_dampener_version([1, 3, 2, 4, 5])
    True

    >>> report_is_safe_dampener_version([9, 7, 6, 2, 1])
    False
    """
    for index_of_level_to_remove in range(0, len(report)):
        report_with_this_level_removed = report[0:index_of_level_to_remove] + report[index_of_level_to_remove + 1:]

        if report_is_safe(report_with_this_level_removed):
            return True
        
    return False

if __name__ == "__main__":
    actual_report_data = parse_raw_csv_data(aocd.get_data(day=2, year=2024))

    print(
        list(map(report_is_safe_dampener_version, actual_report_data)).count(True)
    )