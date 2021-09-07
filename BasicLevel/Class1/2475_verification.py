import sys
result = 0
number = list(map(int, sys.stdin.readline().split()))

for i in number:
    result += (i**2)
print(result%10)