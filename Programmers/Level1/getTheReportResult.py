def solution(id_list, reports, k):
    stop = []
    answer = [0] * len(id_list)
    dicReports = dict()
    for i in set(reports):
        report = i.split(' ')
        stop.append(report[1])
        if report[0] in dicReports:
            dicReports[report[0]].append(report[1])
        else: dicReports[report[0]] = [report[1]]

    stop = set([i for i in stop if stop.count(i) >= k])

    for key, value in dicReports.items():
        for s in stop:
            if s in value:
                answer[id_list.index(key)] += 1
    return answer
        #for v in value:
        #    if v in stop:
        #        answer[id_list.index(key)] += 1


    #stop = list(dicReports.values())
    #stop = [element for i in stop for element in i]
    #print(stop)
    #for i in dicReports.values():



    """
    answer = []
    send = []
    received = []

    for i in reports:
        report = i.split(' ')
        send.append(report[0])
        received.append(report[1])

    result = [received.count(i) if received.count(i) >= k else 0 for i in id_list]
    result = [id_list[i] for i in range(len(id_list)) if result[i]]
    #print(result)

    for i in range(len(result)):
        tmp = [j for j, value in enumerate(received) if value == result[i]]
        for i in tmp:
            id_list.index(result[i])
            answer[i] += 1
    print(answer)

    #print(send)
    """




    """
    info = dict()
    stop = []
    result = [0] * len(id_list)

    info = dict(id_list)
    print(info)
    for i in set(reports):
        report = i.split()
        stop.append(report[1])
        info[report[0]].append(report[1])

    for i in set(stop):
        print(stop.count(i), k)
        if stop.count(i) >= k:
            for key, value in info.items():
                if i in value:
                    result[id_list.index(key)] += 1

    return result
    """

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))