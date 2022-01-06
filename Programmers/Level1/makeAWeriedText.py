def solution(s):
    answer = []
    for i in s.split(' '):
        for j in range(len(i)):
            answer.append(i[j].lower() if j%2 else i[j].upper())
        answer.append(' ')
    return ''.join(answer[:len(s)])