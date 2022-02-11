#시간초과
n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
print('\n'.join(repr(i) for i in sorted(numbers)))