def solution(N, stages):
    person = len(stages)
    result = []
    fail = [stages.count(i) for i in range(1, N + 1)]

    for i in range(len(fail)):
        if not person:
            result.append((0, i + 1))
            continue
        result.append((fail[i] / person, i + 1))
        person -= fail[i]

    result.sort(key=lambda x: (x[0], -x[1]), reverse=True)
    return [i[1] for i in result]