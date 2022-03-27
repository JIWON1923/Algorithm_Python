from collections import deque
result, idx = [], 1
n, k = map(int, input().split())
queue = deque([i for i in range(1, n+1)])
while queue:
    if idx % k == 0: result.append(queue.popleft())
    else: queue.append(queue.popleft())
    idx += 1
print(str(result).replace('[', '<').replace(']', '>'))

