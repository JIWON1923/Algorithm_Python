score = {"S": 1, "D": 2, "T": 3}


def solution(dartResult):
    dartResult = dartResult.replace('10', 'A')
    answer = []
    result = 0
    for i in dartResult:
        if i.isdigit():
            result = int(i)
        elif i.isalpha():
            if i == "A":
                result = 10
            else:
                result **= score[i]
                answer.append(result)
        elif i == "*":
            answer[-1] *= 2
            if len(answer) > 1:
                answer[-2] *= 2
        else:
            answer[-1] *= -1
    return sum(answer)