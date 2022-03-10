apartment = [[0]*15 for _ in range(15)]
apartment[0] = [i for i in range(1, 15)]
for i in range(1, 15):
    for j in range(14):
        if j == 0 : apartment[i][j] = 1
        else:
            apartment[i][j] = apartment[i-1][j] + apartment[i][j-1]
t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    print(apartment[k][n-1])
