import sys
result = 1
cnt = []
for i in range(3):
    result *= int(sys.stdin.readline())
result = list(str(result))
for i in range(10):
    cnt.append(result.count(str(i)))
print("\n".join(repr(i) for i in cnt))