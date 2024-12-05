# chief historian is lost... we have a list of places to check
# after a location is checked, it gets a star
# after 50 stars, we must have found the chief historian
# two puzzles each day, one star for each completed, the second is unlocked after the first is completed

# instructions are to sort each list, and add up the pairwise differences
import operator
import collections

test_lists = [
    [3, 4, 2, 1, 3, 3],
    [4, 3, 5, 3, 9, 3]
]

def sum_of_pairwise_absolute_differences(lists):
     return sum(
        abs(operator.sub(*pair_of_numbers)) for pair_of_numbers in zip(*map(sorted, lists))
    )
    
def calculate_similarity_score(lists):
    # setting up the hash maps takes O(n) time, note that 
    # in theory 
    left_list_occurrences = collections.Counter(lists[0])
    right_list_occurrences = collections.Counter(lists[1])

    total_similarity = 0
    for (location, location_occurrences_left) in left_list_occurrences.items():
        total_similarity += location * location_occurrences_left * right_list_occurrences[location]

    return total_similarity


def read_csv_raw_data(filename):
    raw_csv_data = open('day_1_raw_data.csv')
    
    number_pairs_by_line = [list(map(int, line.split())) for line in raw_csv_data]
    return [
        [number_pair[0] for number_pair in number_pairs_by_line],
        [number_pair[1] for number_pair in number_pairs_by_line],
    ]   

if __name__ == "__main__": 
    actual_lists = read_csv_raw_data("day_1_historian_hysteria.csv")
    # print(sum_of_pairwise_absolute_differences(actual_lists))
    print(calculate_similarity_score(actual_lists))