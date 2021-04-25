row, column = map(int, input().split())

# 2차원 배열 입력받기
cards = [list(map(int, input().split())) for _ in range(column) ]

#각 행에 존재하는 제일 작은 값 넣기
mincard = [] 
for i in range(column):
  mincard.append(min(cards[i]))
# 그 중에 제일 큰 카드 값 찾기
print(max(mincard)기