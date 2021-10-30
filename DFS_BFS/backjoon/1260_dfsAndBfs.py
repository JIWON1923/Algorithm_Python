import sys
read = sys.stdin.readline
from collections import deque


def dfs(graph, visited, v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, visited, i)


def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, read().split())
graph = [[] for _ in range(n+1)]
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)
for i in range(m):
    n1, n2 = map(int, read().split())
    if n2 not in graph[n1]: graph[n1].append(n2)
    if n1 not in graph[n2]: graph[n2].append(n1)
for i in graph:
    i.sort()
dfs(graph, visited_dfs, v)
print()
bfs(graph, visited_bfs, v)


