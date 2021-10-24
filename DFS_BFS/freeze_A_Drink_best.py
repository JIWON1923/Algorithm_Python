n, m = map(int, input().split())

# map 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정 노드 방문 후 연결된 모든 노드 방문
def DFS(x, y):
    # 주어진 범위를 벗어난 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        #방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우 재귀 호출
        DFS(x-1, y)
        DFS(x, y-1)
        DFS(x+1, y)
        DFS(x, y+1)
        return True
    return False
#모든 노드에 대해 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        #현재 위치에서 DFS 수행
        if DFS(i, j) == True:
            result += 1
print(result)