def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        answer.append(arr1[i] | arr2[i])
        answer[i] = "0" * (n - (len(bin(answer[i])) - 2)) + str(bin(answer[i]))[2:]
        answer[i] = answer[i].replace('1', '#')
        answer[i] = answer[i].replace('0', ' ')

    return answer