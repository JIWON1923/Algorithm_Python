n = int(input())
move = list(input().split())
x, y = 1, 1

for i in move:
  x2, y2 = x, y
  if i == 'L': y2 -= 1
  elif i == 'R': y2 += 1
  elif i == 'U': x2 -= 1
  elif i == 'D': x2 += 1
  if x2 >= 1 and x2 <= n : x = x2
  if y2 >= 1 and y2 <= n : y = y2
print(x, y)