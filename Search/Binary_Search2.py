def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
            continue
        else:
            start = mid + 1
            continue
    return None


n, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result is None:
    print("존재하지 않습니다.")
else:
    print(result + 1)