from collections import deque
for _ in range(int(input())):
    result = 1
    l, p = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    while queue:
        if queue[0] == max(queue):
            queue.popleft()
            if p == 0:
                print(result)
                break
            else: result += 1
        else: queue.append(queue.popleft())
        p = len(queue)-1 if p == 0 else p - 1
