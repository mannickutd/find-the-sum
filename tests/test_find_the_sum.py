import pytest
from find_the_sum.find_the_sum import find_the_sum_attempt_1


INPUT_FIXTURES = [
    ([1, 2, 3], True),
    ([1, 1, 1], False),
    ([-1, 0, -1], True),
    ([0, 0, 0], True),
    ([4, 5, 15, 2, 8], False),
    ([8, 7, 5, 3], True),
]


@pytest.mark.parametrize(
    "input_list, has_sum",
    INPUT_FIXTURES,
)
def test_find_the_sum_attempt_1(input_list, has_sum):
    assert find_the_sum_attempt_1(input_list) == has_sum
