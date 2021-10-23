from collections import deque # queue 사용 위한 라이브러리 사용

#BFS 메서드 정의 (Breadth First Search)
def bfs(graph, start, visited):
    queue = deque([start])

    # 현재 노드 방문 처리
    visited[start] = True

    # 큐가 빌 때 까지 반복
    while queue:
        #큐에서 하나 꺼내 출력
        v = queue.popleft()
        print(v, end=' ')

        # 인접 노드 중 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 2차원 리스트로 표현
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 방문 정보를 1차원 리스트로 표현
visited = [False] * len(graph)

#정의된 BFS 호출
bfs(graph, 1, visited)