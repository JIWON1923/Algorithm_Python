import sys
n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
cards = sorted([i for i in cards if i < m], reverse=True)
result, i, j, k = m+1, 0, 1, 2
results = []
while i != len(cards)-2:
    result = cards[i] + cards[j] + cards[k]
    if result <= m: results.append(result)
    k += 1
    if k == len(cards):
        j += 1
        if j == len(cards)-1:
            i += 1
            j = i+1
        k = j+1
print(max(results))
