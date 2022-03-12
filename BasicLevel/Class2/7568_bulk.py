bulks = []
tmp = 0
n = int(input())
result = [1] * n
for i in range(n):
    w, h = map(int, input().split())
    bulks.append([w, h])
for i in range(n):
    bulk = bulks[i]
    for j in bulks:
        if bulk[0] < j[0] and bulk[1] < j[1]:
            result[i] += 1
print(' '.join(repr(i) for i in result))