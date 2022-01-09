"""
<에라토스테네의 체>
여러 개의 수가 소수인지 아닌지 판별할 때 사용
1) 2부터 N까지 모든 자연수 나열
2) 남은 수 중 아직 처리하지 않은 가장 작은 수 찾기
3) 남은 수 중 i의 배수를 모두 제거 (i는 제거하지 않음)
4) 2번, 3번 과정 반복
"""

import math


def eratos(n):
    result = [True for _ in range(n+1)]
    for i in range(2, int(math.sqrt(n)) + 1 ):
        if result[i]:
            j = 2
            while i*j <= n:
                result[i*j] = False
                j += 1
    return [i for i in range(2, n+1) if result[i]]


print(eratos(10)) # 1부터 10 사이의 소수 판별
