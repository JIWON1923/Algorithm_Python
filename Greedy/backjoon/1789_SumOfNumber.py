num = int(input())
temp = 0
result = 0

for i in range(2, num):
    if temp > num: break
    temp += i
    result += 1

if num <= 2: result = 1
if num == 3: result = 2
print(result)