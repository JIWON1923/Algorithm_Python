import sys
k = int(input())
for i in range(k):
    h, w, n = map(int, sys.stdin.readline().split())
    if n % h == 0:
        floor = str(h)
        room = str(n//h).zfill(2)
    else:
        floor = str(n % h)
        room = str(n//h + 1).zfill(2)
    print(floor + room)

