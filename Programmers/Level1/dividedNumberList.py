def solution(arr, divisor):
    result = [i for i in arr if i%divisor == 0]
    if len(result) == 0: return [-1]
    else: return sorted(result)