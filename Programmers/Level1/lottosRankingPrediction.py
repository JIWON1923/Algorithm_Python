#로또의 최고순위와 최저순위
def solution(lottos, win_nums):

    cnt = lottos.count(0)
    result = len(set(lottos).intersection(set(win_nums)))

    best = 7 - (result + cnt) if 7 - (result + cnt) <= 6 else 6
    worst = 7 - result if (7 - result) <= 6 else 6
    answer = [best, worst]

    return answer