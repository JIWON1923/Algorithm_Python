#시간초과
def solution(n, left, right):
    answer = ""
    num = [i for i in range(1, n + 1)]
    for i in range(1, n+1):
        for j in range(i):
            num[j] = i
        answer += ' '.join(map(str, num)) + ' '
    answer = list(map(int, answer.split()))
    return answer[left: right+1]

# 1 2 3
# 2 2 3
# 3 3 3