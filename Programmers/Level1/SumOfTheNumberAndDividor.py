def solution(left, right):
    result = 0
    for i in range(left, right + 1):
        result += dividor(i)
    return result

def dividor(n):
    result = len([i for i in range(1, n+1) if not n%i])
    return -n if result%2 else n