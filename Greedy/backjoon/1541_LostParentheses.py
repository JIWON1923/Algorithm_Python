expression = input().split('-')
plus = []
result_plus = []
result = 0

for i in expression:
    plus = i.split('+')
    num = 0
    for j in plus:
        num += int(j)
    result_plus.append(num)

result = result_plus[0]

for i in range(1, len(expression)):
    result -= result_plus[i]
print(result)
