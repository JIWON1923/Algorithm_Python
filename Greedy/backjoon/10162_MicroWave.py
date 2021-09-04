time_list = [300, 60, 10] # 5분, 1분, 10초
result = [0, 0, 0] # a, b, c 결과 값
t = int(input())

for i in range(3):
    result[i] = t//time_list[i] # 결과 값 = 몫
    t = t % time_list[i] # 다음 t = 나머지

if t == 0: # t가 모두 나누어떨어졌다면
    print(" ".join(repr(i)for i in result))
else: #아니라면
    print(-1)