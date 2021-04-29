location = input()
col = ord(location[0]) - ord('a')
row = int(location[1])
count = 0
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, 1, -1]

for i in range(8):
  if col + dx[i] >= 0 and col + dx[i] <= 8:
    if row + dy[i] >= 1 and row + dy[i] <=8:
      count += 1
print(count)