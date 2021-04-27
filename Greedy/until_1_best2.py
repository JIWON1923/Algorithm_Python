n, k = map(int, input().split())
result = 0

while True:
  # N==K로 나누어떨어지는 수가 될 때 까지 1씩 빼기
  target = (n // k) * k
  result += (n - target)
  n = target

  #N이 K보다 작을 때(더이상 나눌 수 없을 때) 반복문 탈출
  if n < k:
    break
  
  result += 1
  n //= k

result += (n - 1)
print(result)