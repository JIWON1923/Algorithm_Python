nums = ["zero", "one", "two", "three", "four", "five",
        "six", "seven", "eight", "nine"]


def solution(s):
    for num in range(len(nums)):
        s = s.replace(nums[num], str(num))

    return int(s)