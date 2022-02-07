n = int(input())
result = []
for i in range(n):
    num = int(input())
    if num != 0:
        result.append(num)
    else:
        result.pop(-1)
print(sum(result))