import sys
a, b, v = map(int, sys.stdin.readline().split())
result = (v-b) // (a-b)
if (v-b) % (a-b): result += 1
print(result)