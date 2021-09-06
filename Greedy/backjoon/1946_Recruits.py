case = int(input())
result = []
for i in range(case):
    score = []
    cnt = 1
    applicant = int(input())
    for i in range(applicant):
        score.append(list(map(int, input().split())))
    score = sorted(score, key=lambda x: x[0])
    high_score = score[0][1]
    for j in range(applicant):
        if high_score > score[j][1]: # 높은 등
            cnt += 1
            high_score = score[j][1]
    result.append(cnt)
print(" ".join(repr(i)for i in result))