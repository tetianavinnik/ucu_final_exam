from typing import List, Tuple
from testing import TestError

def test_from_str(test: str) -> List[Tuple[str, str]]:
 return list(map(lambda x: tuple(x.split(' ')), filter(None, test.split('\n'))))


def calc_noncanonicity(timeline: List[Tuple[str, int]]) -> int:
    max_noncanonicity = 0
    requests = {}
    for idx, (event, user) in enumerate(timeline):
        if event == 'REQUEST':
            if user not in requests:
                requests[user] = []
            requests[user].append(idx)
        else:
            request_time = requests[user].pop(0)
            max_noncanonicity = max(max_noncanonicity, idx - request_time)

    return max_noncanonicity


def run_test(test: str, module):
    test = test_from_str(test)
    get_noncanonicity = getattr(module, 'get_noncanonicity')
    result = get_noncanonicity(test)
    if result is None:
        raise TestError("Returned none")
    correct_answer = calc_noncanonicity(test)
    if result != correct_answer:
        raise TestError("Incorrect noncanonicity")
