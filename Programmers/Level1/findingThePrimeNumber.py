import math
def solution(n):
    result = [True for _ in range(n+1)]
    for i in range(2, int(math.sqrt(n)) + 1):
        if result[i]:
            j = 2
            while i*j <= n:
                result[i*j] = False
                j += 1
    return len([i for i in range(2, n+1) if result[i]])