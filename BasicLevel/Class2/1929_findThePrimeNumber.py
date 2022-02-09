m, n = map(int, input().split())
primeNumber = set(range(2, n+1))
for i in range(n):
    if i in primeNumber:
        primeNumber -= set(range(i*2, n+1, i))
for i in sorted(primeNumber):
    if i >= m:
        print(i)