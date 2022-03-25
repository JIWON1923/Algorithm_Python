from collections import deque
import sys
input = sys.stdin.readline
deque = deque()
for i in range(int(input())):
    cmd = input().split()
    if cmd[0] == "push_front":
        deque.appendleft(int(cmd[1]))
    elif cmd[0] == "push_back":
        deque.append(int(cmd[1]))
    elif cmd[0] == "pop_front":
        print(deque.popleft() if len(deque) else -1)
    elif cmd[0] == "pop_back":
        print(deque.pop() if len(deque) else -1)
    elif cmd[0] == "size":
        print(len(deque))
    elif cmd[0] == "empty":
        print(0 if len(deque) else 1)
    elif cmd[0] == "front":
        print(deque[0] if len(deque) else -1)
    else:
        print(deque[-1] if len(deque) else -1)