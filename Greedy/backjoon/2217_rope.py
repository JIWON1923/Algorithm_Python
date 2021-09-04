n = int(input()) # 줄 수
rope = [] # 무게를 넣을 배열

for i in range(n): # 줄 수만큼 반복 입력 받음
    rope.append(int(input()))
rope.sort() # 오름차순으로 정렬

weight = rope[0] * n #제일 작은 로프 수 * 줄 수
for i in range(len(rope)):
    if ( (n-i) * rope[i] > weight ): #n개 중 x개 제거 -> 무게 * (m-x) : 들 수 있는 무게
        weight = (n-i)*rope[i] # 최대 구하기
print(weight) # 출력

