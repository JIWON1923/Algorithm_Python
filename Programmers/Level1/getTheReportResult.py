def solution(id_list, reports, k):
    dic_report = {id: [] for id in id_list}
    answer = [0] * len(id_list)
    for report in set(reports):
        report = report.split(' ')
        dic_report[report[1]].append(report[0])

    for key, value in dic_report.items():
        if len(value) >= k:
            for v in value:
                answer[id_list.index(v)] += 1

    return answer


"""
시간초과
def solution(id_list, reports, k):
    stop = []
    answer = [0] * len(id_list)
    dicReports = {id: [] for id in id_list}
    for i in set(reports):
        report = i.split(' ')
        stop.append(report[1])
        dicReports[report[0]].append(report[1])

    stop = set([i for i in stop if stop.count(i) >= k])

    for key, value in dicReports.items():
        for s in stop:
            if s in value:
                answer[id_list.index(key)] += 1
    return answer
"""