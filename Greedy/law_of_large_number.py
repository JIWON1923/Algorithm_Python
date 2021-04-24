n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort (reverse=True)
result = 0

for i in range(m):
  if k%(i+1) != 0: result += num_list[0]
  else: result += num_list[1]
print(result)