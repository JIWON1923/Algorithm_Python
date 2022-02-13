import sys
n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
start, end = 0, max(trees)

while start <= end:
    mid = (start + end) // 2
    total = sum([i-mid for i in trees if i > mid])
    if total < m:
        end = mid-1
    else:
        result = mid
        start = mid + 1
print(result)