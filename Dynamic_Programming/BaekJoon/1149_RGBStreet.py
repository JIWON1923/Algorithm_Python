house, d = [], []
n = int(input())
for _ in range(n):
    house.append(list(map(int, input().split())))
    d.append([0]*3)
d[0] = house[0]
for i in range(1, len(house)):
    d[i][0] = min(d[i-1][1], d[i-1][2]) + house[i][0]
    d[i][1] = min(d[i-1][0], d[i-1][2]) + house[i][1]
    d[i][2] = min(d[i-1][0], d[i-1][1]) + house[i][2]
print(min(d[n-1]))