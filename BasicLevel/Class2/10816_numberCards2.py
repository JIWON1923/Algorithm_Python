import sys
n = int(sys.stdin.readline())
numbers = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
find = list(map(int, sys.stdin.readline().split()))


def binary_search(target, isUpper):
    start, end = 0, n
    while start < end:
        mid = (start + end) // 2
        if numbers[mid] == target:
            if isUpper: start = mid + 1
            else: end = mid
        elif numbers[mid] > target:
            end = mid
        else:
            start = mid + 1
    return start


result = []
for i in find:
    result.append(binary_search(i, True) - binary_search(i, False))
print(*result)