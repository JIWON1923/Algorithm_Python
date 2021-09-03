coin_list = [500, 100, 50, 10, 5, 1]
charge = int(input())
change = 1000 - charge
result = 0

for coin in coin_list:
    if coin <= change:
        result += change//coin
        change %= coin
print(result)