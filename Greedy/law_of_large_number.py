n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort (reverse=True)

count = m//(k+1)
result = count * num_list[1]
result += (m-count) * num_list[0]
print(result)
