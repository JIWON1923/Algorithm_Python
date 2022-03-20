"""
1. chess판 입력받기
2. (W로 시작하는 경우, B로 시작하는 경우에 따라 결괏값 기록
3. 8 * 8 사이즈 일 경우를 파악
"""
n, m = map(int, input().split())
compare1, compare2 = 'WB' * 25, 'BW' * 25
chess = [[0]*m for _ in range(n)]
result1 = []
for i in range(n):
    value = input()
    if i % 2 == 0: c = compare1
    else: c = compare2
    for j in range(m):
        if value[j] != c[j]: chess[i][j] = 1
for row in range(n-7):
    for col in range(m-7):
        result = 0
        for i in range(8):
            result += sum(chess[row+i][col:col+8])
        result1.append(result)
        result1.append(64-result)
print(min(result1))
