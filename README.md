# Algorithm

## 알고리즘
- [Greedy](#greedy)
- [Implement](#implement)
- [DFS/BFS](#dfs/bfs)
- [Sort](#sort)
- [Binary Search](#binary-search)
- [Dynamic Programming](#dynamic-programming)
- [Shortest Path](#shortest-path)
- [Graph](#graph)
- [기타](#기타)

## [프로그래머스](https://github.com/JIWON1923/Algorithm/tree/master/Programmers)


## Greedy
- 현재 상황에서 지금 당장 좋은 것만 고르는 방법
- 나중에 미칠 영향은 고려하지 않는다.
- 창의력, 최소한의 아이디어 능력을 검증하기 위해 출제되는 문제
- '가장 큰 순서', '가장 작은 순서' 등의 기준이 제시된다.

- 예제
    - 거스름돈 ( change.py )
    - 큰 수의 법칙 ( law_of_large_number.py )
    - 숫자 카드 게임 ( number_card_game.py )
    - 1이 될 때 까지 ( until_1.py )

---
## Implement (구현)
- 완전 탐색 : 모든 경우의 수를 주저 없이 다 계산하는 방법
- 시뮬레이션 : 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행하는 방법
 - 언어 문법을 잘 이해하고, 경험이 있어야 바로 떠올릴 수 있다.
- 사소한 입력조건이 명시되고, 문제의 길이가 꽤 길다.
- Pypy3를 지원한다면, 이를 이용해서 제출하자. (실행시간 줄어듦)

- 예제
    - 상하좌우 ( Top_Down_Left_Right.py )
    - 시각 ( time.py )
    - 왕실의 나이트 ( royal_night.py )
    - 게임 개발 ( game_development.py )

---
## DFS/BFS
### DFS(Depth-First Search)
- 깊이 우선 탐색으로, 그래프의 깊은 부분을 우선적으로 탐색한다.
- 알고리즘
    - 탐색 시작 노드를 스택에 삽입하고 방문처리한다.
    - 스택의 최상단 노드에 방문하지 않은 인접노드가 있다면, 그 인접노드를 스택에 넣고 방문처리한다. 방문하지 않은 인접노드가 없다면, 스택에서 최상단 노드를 꺼낸다.
    - 2번 과정을 수행할 수 없을 때까지 반복한다.
    
    
    ```python
    def dfs(graph, v, visited):
        visited[v] = True
        print(v, end=' ')
        for i in graph[v]:
            if not visitied[i]:
                dfs(graph, i, visited)
    ```
    

### BFS(Breadth-First Search)
- 너비 우선 탐색으로, 가까운 노드부터 탐색하는 알고리즘이다.
- 알고리즘
    - 탐색 시작 노드를 큐에 삽입하고 방문처리한다.
    - 큐에서 노드를 꺼내 해당 노드의 인접노드 중 방문하지 않은 노드를 모두 삽입한다.
    - 2번의 과정을 수행할 수 없을 때까지 반복한다.

    ```python
    from collections import deque
    
    def bfs(graph, start, visited):
        queue = deque([start])
        visited[start] = True
        
        while queue:
            v = queue.popleft()
            print(v, end=' ')
            for i in graph[v]:
                if not visitied[i]:
                    queue.append(i)
                    visited[i] = True
    ```
    
    
## Sort

## Binary Search

## Dynamic Programming

## Shortest Path

## Graph

## 기타
- 소수 찾기
    - math.sqrt를 사용하여 시간 복잡도 단축
- 에라토스테네스의 체
    - 여러 개의 수가 소수인지 아닌지 판별
    - O(NloglogN)
    - 메모리가 많이 필요하다.
    - 1,000,000이내로 주어지는 경우에 사용한다.
        - 이론상 400만 번 정도의 연산으로 해결 가능
         
## Programmers
