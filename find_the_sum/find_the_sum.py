from typing import *


def find_the_sum_attempt_1(input_sequence: Sequence[int]) -> bool:
    '''
        First attempt loop through all values in 2 loops testing if the sum
        is contained within the original list. 
        Complexity O(n^2).
        Use a set for looking up sum because it works as a hash list.
    '''
    input_set: Set = set(input_sequence)
    for i, x in enumerate(input_sequence):
        for m, y in enumerate(input_sequence):
            if i != m and (x + y in input_set):
                return True
    return False


def _find_number_in_sequence(base: int,
                             input_sequence: Sequence[int],
                             input_set: Set[int],
) -> bool:
    for y in input_sequence:
        total: int = base + y
        if total in input_set:
            return True
        # Don't need to continue searching if the next sum is
        # greater than the last element in the list
        if total > input_sequence[-1]:
            return False
    return False


def find_the_sum_attempt_2(input_sequence: Sequence[int]) -> bool:
    '''
        Second attempt sort the input_sequence before starting to loop through the sequence.
        Use a set for looking up sum because it works as a hash list.
    '''
    input_set: Set = set(input_sequence)
    # Check if set is all the same
    input_set_length = len(input_set)
    if input_set_length == 1 and input_sequence[0] != 0:
        return False
    elif input_set_length == 1 and input_sequence[0] == 0:
        return True
    sorted_sequence = sorted(input_sequence)
    for i, x in enumerate(sorted_sequence):
        search_list = sorted_sequence[:i] + sorted_sequence[i + 1:]
        if _find_number_in_sequence(
            x,
            search_list,
            input_set,
        ):
            return True
    return False

