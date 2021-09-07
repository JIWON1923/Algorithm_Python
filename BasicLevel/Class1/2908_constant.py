a, b = list(input().split())
result = a[::-1] if a[::-1] > b[::-1] else b[::-1]
print(int(result))