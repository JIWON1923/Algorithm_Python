n, m = map(int, input().split())
value = 0

for i in range(n):
    data = list(map(int, input().split()))
    if value < min(data):
        value = min(data)
print(data)
