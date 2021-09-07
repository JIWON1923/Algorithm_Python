import sys
number = []
for i in range(9):
    number.append(int(sys.stdin.readline()))
print(max(number))
print(number.index(max(number)) + 1)