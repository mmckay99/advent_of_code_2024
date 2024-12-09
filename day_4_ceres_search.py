import aocd # type: ignore
import itertools

test_wordsearch_data_string = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

def parse_wordsearch_string(wordsearch_data_string):
    return list(map(list, wordsearch_data_string.strip().split('\n')))

def count_cross_mas_occurrences(wordsearch_data):
    table_width = len(wordsearch_data[0])
    table_height = len(wordsearch_data)

    found_occurrences = 0

def count_xmas_word_occurrences(wordsearch_data):
    table_width = len(wordsearch_data[0])
    table_height = len(wordsearch_data)

    found_occurrences = 0

    # for each table cell, if it contains 'X' or 'S' then it could be the end
    # of an XMAS/SAMX occurrence, going either horizontal, vertical,
    # left diagonal, or right diagonal (so there are 2*4=8 total possible orientations
    for i, j in itertools.product(range(0, table_height), range(0, table_width)):
        if wordsearch_data[i][j] not in ['X', 'S']:
            continue

        words_going_down_or_left_ending_here = [
            (wordsearch_data[i][j] + wordsearch_data[i][j - 1] + wordsearch_data[i][j - 2] + wordsearch_data[i][j - 3]) if j > 2 else None,
            (wordsearch_data[i][j] + wordsearch_data[i - 1][j] + wordsearch_data[i - 2][j] + wordsearch_data[i - 3][j]) if i > 2 else None,
            (wordsearch_data[i][j] + wordsearch_data[i - 1][j - 1] + wordsearch_data[i - 2][j - 2] + wordsearch_data[i - 3][j - 3]) if (i > 2 and j > 2) else None,
            wordsearch_data[i][j] + wordsearch_data[i - 1][j + 1] + wordsearch_data[i - 2][j + 2] + wordsearch_data[i - 3][j + 3] if (i > 2 and j < table_width - 3) else None
        ]

        found_occurrences += words_going_down_or_left_ending_here.count("XMAS") + words_going_down_or_left_ending_here.count("SAMX")

    return found_occurrences

if __name__ == "__main__":
    actual_wordsearch_data_string = aocd.get_data(day=4, year=2024)
    xmas_word_occurrences = count_xmas_word_occurrences(parse_wordsearch_string(actual_wordsearch_data_string))
    print(xmas_word_occurrences)