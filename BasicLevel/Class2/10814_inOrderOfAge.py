import sys
n = int(sys.stdin.readline())
info = []
for i in range(n):
    info.append(list(input().split()))
info.sort(key=lambda x: int(x[0]))
for i in info:
    print(' '.join(i))