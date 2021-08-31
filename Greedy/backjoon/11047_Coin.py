n, k = map(int, input().split())
coin_list=[]
for i in range(n):
    coin_list.append(int(input()))
coin_list.reverse()
result = 0
for coin in coin_list:
    if k < coin:
        continue
    elif k >= coin:
        result += k // coin
        k %= coin
print(result)