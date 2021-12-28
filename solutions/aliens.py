import copy

def calc_systems_count(num: int) -> int:
    new_nums = []
    count = 0
    for i in range(2, num):
        num_temp = copy.deepcopy(num)
        new_num = ''
        while num_temp>0:
            new_num = str(num_temp % i) + new_num
            num_temp //= i
        if new_num == new_num[::-1]:
            count += 1
            print(new_num)
        # new_nums.append(new_num)
    return count
