# 이항계수
"""
      1
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1
 1 5 10 10 5 1
1 6 15 20 15 6 1
"""
# binomial = [[1]*i for i in range(12)]
# for i in range(2, 12):
#     for j in range(i):
#         if j == 0 or j == i-1:
#             binomial[i][j] = 1
#         else:
#             binomial[i][j] = binomial[i-1][j-1] + binomial[i-1][j]
top, down = 1, 1
n, k = map(int, input().split())
for i in range(k):
    top *= (n-i)
    down *= (k-i)
print(top//down)