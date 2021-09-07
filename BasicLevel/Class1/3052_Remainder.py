import sys
num = set()
for _ in range(10):
    num.add(int(sys.stdin.readline())%42)
print(len(num))