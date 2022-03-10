import sys
result = 0
n = int(sys.stdin.readline())
for i in range(n):
    value = i + sum(list(map(int, str(i))))
    if value == n:
        result = i
        break
print(result)