num = int(input())
result, cnt = 0, 0

for i in range(1, num): # 0, 1, 2, 3, 4
    cnt += 1
    result += i
    if result >= num : break

if result == num : print(cnt)
elif result > num : print(cnt-1)
elif result < 3 : print(1)