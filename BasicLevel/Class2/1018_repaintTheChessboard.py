"""
1. chess판 입력받기
   1-1 WB, BW를 입력받아, 각 줄과 다른 결과가 있다면 1을 더함
       (같은 경우는 0임)
2. 8 * 8 사이즈 일 경우를 파악
    2-1 8줄씩 잘라서 각 리스트의 합을 구함
    2-2 8*8 을 v라 했을 때, v와 64-v 값을 result1에 삽입(W먼저 시작하는 경우의 수 파악)
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
