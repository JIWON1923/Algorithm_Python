from itertools import combinations
def solution(nums):
    result = 0
    new_nums = [sum(i) for i in (combinations(nums, 3))]
    eratos = set(range(2, max(new_nums) + 1))
    for i in range(max(new_nums)+1):
        if i in eratos:
            eratos -= set(range(i * 2, max(new_nums) + 1, i))
            if i in new_nums:
                result += new_nums.count(i)
    return result