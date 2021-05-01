n, m = map(int, input().split())
a, b, d = map(int, input().split())
input_data = list(map(int, input().split()) for _ in range(m))

direction = [0,1,2,3]
move_type = [(0,-1), (-1,0), (0,1), (1,0)]
count = 0

while(1):

  for i in direction:
    if i == d:
      d += 1
      for move in move_type:
        da = a + move[1]
        db = b + move[0]

        if input_data[db, da] == 0:
          a = da
          b = db
          input_data[b][a] = 1
          count += 1

        elif input_data[db, da] == 1:
          d += 1

  da = move_type[d][1]
  db = move_type[d][0]
  if (input_data[db, da] == 0):
    a = da
    b = db
    input_data[b][a] = 1
    count += 1

  else: break

print(count)