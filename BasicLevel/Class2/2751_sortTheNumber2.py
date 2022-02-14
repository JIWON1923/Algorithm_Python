#시간초과
import sys
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(sys.stdin.readline()))
print('\n'.join(repr(i) for i in sorted(numbers)))