# 시간초과
def solution(n, left, right):
    answer = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            answer.append(i) if i > j else answer.append(j)
    return answer[left:right+1]