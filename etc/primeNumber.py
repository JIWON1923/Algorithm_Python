import math

# 소수 판별 함수
def is_prime_number(x):
    #2부터 x의 제곱근까지의 모든 수 확인
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0: #특정 수로 나누어떨어지면
            return False # 소수가 아님
    return True

print(is_prime_number(4))
print(is_prime_number(7))