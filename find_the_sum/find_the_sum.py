from typing import *


def find_the_sum_attempt_1(input_sequence: Sequence[int]) -> bool:
    '''
        First attempt loop through all values in 2 loops testing if the sum
        is contained within the original list. 
        Complexity O(n^2).
    '''
    input_set: Set = set(input_sequence)
    for i, x in enumerate(input_sequence):
        for m, y in enumerate(input_sequence):
            if i != m and (x + y in input_set):
                return True
    return False
