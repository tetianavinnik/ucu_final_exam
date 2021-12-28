from testing import TestError

def calc_systems_count(num: int):
    cnt = 0
    for number_system in range(2, num):
        vals = []
        num_copy = num
        while num_copy > 0:
            vals.append(num_copy % number_system)
            num_copy //= number_system
        if vals == vals[::-1]:
            cnt += 1
    return cnt


def run_test(test: str, module):
    get_systems_count = getattr(module, 'get_systems_count')
    correct_answer = calc_systems_count(int(test))
    result = get_systems_count(int(test))
    if result is None:
        raise TestError("Returned none")
    if result != correct_answer:
        raise TestError("Incorrect systems count")
