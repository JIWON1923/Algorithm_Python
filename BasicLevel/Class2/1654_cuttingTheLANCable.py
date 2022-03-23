import sys
k, n = map(int, input().split())
cables = [int(sys.stdin.readline()) for _ in range(k)]
start, end = 1, max(cables)
while start <= end:
    mid, cnt = (start + end) // 2, 0
    for i in cables:
        cnt += i//mid
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)