fibo = [[0, 0] for _ in range(41)]
fibo[0][0] = 1
fibo[1][1] = 1
t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(2, n+1):
        if sum(fibo[i]) == 0:
            fibo[i][0] = fibo[i-1][0] + fibo[i-2][0]
            fibo[i][1] = fibo[i-1][1] + fibo[i-2][1]
    print(' '.join(repr(i) for i in fibo[n]))
