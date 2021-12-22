def solution(d, budget):
    answer = 0
    for i in sorted(d):
        budget -= i
        if budget < 0: return answer
        answer += 1
    return answer