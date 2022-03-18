import sys
int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
int(sys.stdin.readline())
find = list(map(int, sys.stdin.readline().split()))
numbers.sort()
for target in find:
    start, end, result = 0, len(numbers)-1, False
    while start <= end:
        mid = (start + end) // 2
        if numbers[mid] == target:
            result = True
            break
        elif numbers[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    print(1 if result else 0)



# 시간초과
# n = int(input())
# nums = set(map(int, input().split()))
# m = int(input())
# find = list(map(int, input().split()))
# result = list(set(find) - nums)
# print('\n'.join(['0' if i in result else '1' for i in find]))