change = int(input())
coin = [500, 100, 50, 10]
i, result = 0, 0
while (change != 0 and i < 4):
  if change >= coin[i]:
    change -= coin[i]
    result += 1
  else:
    i += 1
print (result)