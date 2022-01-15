def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        result = []
        for j in range(len(arr1[i])):
            result.append(arr1[i][j] + arr2[i][j])
        answer.append(result)
    return answer