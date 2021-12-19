def solution(array, commands):
    results = []
    for i in range(len(commands)):
        result = sorted(array[commands[i][0]-1:commands[i][1]])
        results.append(result[commands[i][2]-1])
    return results