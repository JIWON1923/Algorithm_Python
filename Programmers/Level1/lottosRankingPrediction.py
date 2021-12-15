#로또의 최고순위와 최저순위
def solution(lottos, win_nums):
    result = 0

    cnt = lottos.count(0)
    if cnt != 0:
        lottos.remove(0)

    for num in lottos:
        if num in win_nums:
            result += 1
            win_nums.remove(num)

    best = 7 - (result + cnt) if 7 - (result + cnt) <= 6 else 6
    worst = 7 - result if (7 - result) <= 6 else 6
    answer = [best, worst]

    return answer