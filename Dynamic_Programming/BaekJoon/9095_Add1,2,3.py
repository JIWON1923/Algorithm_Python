num = [0] * 12
num[1], num[2], num[3] = 1, 2, 4
for i in range(4, 12):
    num[i] = num[i-3] + num[i-2] + num[i-1]
t = int(input())
for i in range(t):
    print(num[int(input())])