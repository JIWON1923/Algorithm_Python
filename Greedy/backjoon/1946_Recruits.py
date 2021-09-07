import sys
case = int(input())
for _ in range(case):
    applicant = int(input())
    score = sorted([list(map(int, sys.stdin.readline().strip().split())) for x in range(applicant)], key=lambda x:x[0])
    result = 1
    high_score = score[0][1] # = 작은 숫자의 등수(높은 점수)

    for i in range(1, applicant):
        if high_score > score[i][1]: # 점수가 더 높으면
            high_score = score[i][1]
            result += 1
    print(result)