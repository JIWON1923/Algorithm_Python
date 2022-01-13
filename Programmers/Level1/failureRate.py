# 투포인터 연습 후 커밋하기 !!

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

fail = [stages.count(i) for i in range(1, N+1)]
result = []
person = len(stages)
for i in fail:
    result.append(i/person)
    person -= i
print(fail)
print(result)