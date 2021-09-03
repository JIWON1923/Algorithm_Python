n = int(input())
meet = []
for i in range(n):
    room = list(map(int, input().split()))
    meet.append(room)
meet = sorted(meet, key=lambda x : x[0])
meet = sorted(meet, key=lambda x : x[1]) #회의 일찍 끝나는 순으로 정렬
compare = meet[0][1]
result = 1
for i in range(1, n):
    if compare <= meet[i][0]:
        compare = meet[i][1]
        result += 1
print(result)