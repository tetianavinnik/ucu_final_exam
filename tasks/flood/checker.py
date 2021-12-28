from typing import List, Tuple
from testing import TestError

def test_from_str(test: str) -> List[Tuple[str, str]]:
    return list(map(int, filter(None, test.split(' '))))


def calc_amount_of_water(heights: List[int]):
    left_dp = [0 for _ in heights]
    for i in range(len(heights)):
        left_dp[i] = max(left_dp[i - 1] if i > 0 else 0, heights[i])
    right_dp = [0 for _ in heights]
    for i in range(len(heights)):
        idx = len(heights) - i - 1
        right_dp[idx] = max(right_dp[idx + 1] if idx < (len(heights) - 1) else 0, heights[idx])
    water = 0
    for idx, height in enumerate(heights):
        water += min(left_dp[idx], right_dp[idx]) - height
    return water


def run_test(test: str, module):
    test = test_from_str(test)
    get_amount_of_water = getattr(module, 'get_amount_of_water')
    result = get_amount_of_water(test)
    if result is None:
        raise TestError("Returned none")
    correct_answer = calc_amount_of_water(test)
    if result != correct_answer:
        raise TestError("Incorrect amount of water")
