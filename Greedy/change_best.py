change = int(input())
cnt = 0
coin_types = [500, 100, 50, 10] #큰 단위부터

for coin in coin_types:
  cnt += change//coin # 거슬러줄 수 있는 동전의 개수 (큰 단위부터)
  change %= coin # 나머지
print (cnt)