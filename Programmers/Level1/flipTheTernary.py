def solution(n):
    answer = []
    while(n>0):
        answer.append(n%3)
        n //= 3
    answer.reverse() # 3진법 표현
    return sum([(3**i)*answer[i] for i in range(len(answer))])