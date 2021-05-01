#n 입력받기
n = int(input())
move = list(input().split()) #계획
x, y = 1, 1 #초기 위치

for i in move: #계획 탐색
  x2, y2 = x, y #x2, y2에 현재위치 복사
  if i == 'L': y2 -= 1
  elif i == 'R': y2 += 1
  elif i == 'U': x2 -= 1
  elif i == 'D': x2 += 1
  #움직일 수 있다면 현재 위치 변경
  if x2 >= 1 and x2 <= n : x = x2
  if y2 >= 1 and y2 <= n : y = y2
print(x, y)