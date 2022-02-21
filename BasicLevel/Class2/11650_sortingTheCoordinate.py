import sys
n = int(sys.stdin.readline())
coordinate = []
for i in range(n):
    coordinate.append(list(map(int, sys.stdin.readline().split())))
coordinate.sort(key=lambda x: (x[0], x[1]))
for i in coordinate:
    for j in i:
        print(j, end=' ')
    print()