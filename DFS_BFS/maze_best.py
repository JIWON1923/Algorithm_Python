from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#BFS 구현
def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4): #현재 위치에서 4 방향
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간 벗어나면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 처음 방문하는 경우만 최단거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]
#BFS 결과 출력
print(BFS(0,0))