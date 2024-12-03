# chief historian is lost... we have a list of places to check
# after a location is checked, it gets a star
# after 50 stars, we must have found the chief historian
# two puzzles each day, one star for each completed, the second is unlocked after the first is completed

# instructions are to sort each list, and add up the pairwise differences
import operator

test_lists = [
    [3, 4, 2, 1, 3, 3],
    [4, 3, 5, 3, 9, 3]
]

def sum_of_pairwise_absolute_differences(lists):
     return sum(
        abs(operator.sub(*pair_of_numbers)) for pair_of_numbers in zip(*map(sorted, lists))
    )
    
if __name__ == "__main__":
    with open('day_1_raw_data.csv') as raw_csv_data:
        number_pairs_by_line = [list(map(int, line.split())) for line in raw_csv_data]
        actual_lists = [
            [number_pair[0] for number_pair in number_pairs_by_line],
            [number_pair[1] for number_pair in number_pairs_by_line],
        ]

        print(sum_of_pairwise_absolute_differences(actual_lists))