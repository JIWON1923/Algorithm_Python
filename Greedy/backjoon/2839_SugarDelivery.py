n = int(input()) #설탕 무게
cnt = 0
while True:
    if n < 3:
        cnt = -1
        break
    if n % 5 != 0:
        n -= 3
        cnt += 1
    elif n % 5 == 0:
        cnt += (n//5)
        break
    if n == 0: break
print(cnt)