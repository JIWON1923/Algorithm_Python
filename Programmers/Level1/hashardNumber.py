def solution(number):
    return "true" if number % sum([int(i) for i in str(number)]) == 0 else "false"