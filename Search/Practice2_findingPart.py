def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
            continue
        else:
            end = mid - 1
            continue
    return None


n = int(input())
array = list(map(int, input().split()))
m = int(input())
parts = list(map(int, input().split()))

array.sort()
for find in parts:
    result = binary_search(array, find, 0, n-1)
    if result is None: print('no', end=' ')
    else: print('yes', end=' ')