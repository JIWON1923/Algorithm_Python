n, m = map(int, input().split())
a, b, d = map(int, input().split())
input_data = [list(map(int, input().split())) for _ in range(m)]

direction = [ (-1,0), (0,1), (1,0), (0,-1) ]
input_data[a][b] = 1
count = 1
turn = 0

def left():
  global d
  d -= 1
  if d <= 0: d = 3

while True:
  left()
  da = a + direction[d][0]
  db = b + direction[d][1]

  if input_data[da][db] == 0:
    input_data[da][db] = 1
    count += 1
    turn = 0
    a, b = da, db

  else: 
    turn += 1
  
  if turn == 4:
    da = a + direction[d][0] * -1
    db = b + direction[d][1] * -1
    if input_data[da][db] == 0:
      input_data[da][db] = 1
      count += 1
      turn = 0
      a, b = da, db
    else: 
      break

print(count)