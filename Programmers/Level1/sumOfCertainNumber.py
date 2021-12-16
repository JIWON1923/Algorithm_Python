def solution(numbers):
    basic = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    numbers = set(numbers)
    result = basic - numbers
    return sum(result)