import sys
numbers = [0] * 10001
for i in range(int(sys.stdin.readline())):
    numbers[int(sys.stdin.readline())] += 1
for i in range(len(numbers)):
    if numbers[i] != 0:
        for j in range(numbers[i]):
            print(i)
# 시간초과
# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[0]
#     tail = arr[1:]
#     leftSide = [x for x in tail if x <= pivot]
#     rightSide = [x for x in tail if x > pivot]
#     return quicksort(leftSide) + [pivot] + quicksort(rightSide)
#
#
# number = []
# for i in range(int(input())):
#     number.append(int(input()))
# print('\n'.join(repr(x) for x in quicksort(number)))