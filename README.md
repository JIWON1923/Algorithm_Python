# Algorithm

## 알고리즘
- [Greedy](#greedy)
- [Implement](#implement)
- [DFS/BFS](#dfs-bfs)
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
    - [거스름돈](https://github.com/JIWON1923/Algorithm/blob/master/Greedy/change.py)
    - [큰 수의 법칙](https://github.com/JIWON1923/Algorithm/blob/master/Greedy/law_of_large_number.py)
    - [숫자 카드 게임](https://github.com/JIWON1923/Algorithm/blob/master/Greedy/number_card_game.py)
    - [1이 될 때 까지](https://github.com/JIWON1923/Algorithm/blob/master/Greedy/until_1.py)

---
## Implement
- 완전 탐색 : 모든 경우의 수를 주저 없이 다 계산하는 방법
- 시뮬레이션 : 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행하는 방법
 - 언어 문법을 잘 이해하고, 경험이 있어야 바로 떠올릴 수 있다.
- 사소한 입력조건이 명시되고, 문제의 길이가 꽤 길다.
- Pypy3를 지원한다면, 이를 이용해서 제출하자. (실행시간 줄어듦)

- 예제
    - [상하좌우](https://github.com/JIWON1923/Algorithm/blob/master/Implement/Top_Down_Left_Right.py)
    - [시각](https://github.com/JIWON1923/Algorithm/blob/master/Implement/time.py)
    - [왕실의 나이트](https://github.com/JIWON1923/Algorithm/blob/master/Implement/royal_night.py)
    - [게임 개발](https://github.com/JIWON1923/Algorithm/blob/master/Implement/game_develpment.py)

---
## DFS-BFS
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
   
    
    
- 예제
    - [DFS](https://github.com/JIWON1923/Algorithm/blob/master/DFS_BFS/DFS.py)
    - [BFS](https://github.com/JIWON1923/Algorithm/blob/master/DFS_BFS/BFS.py)
    - [음료수 얼려 먹기](https://github.com/JIWON1923/Algorithm/blob/master/DFS_BFS/freeze_A_Drink_best.py)
    - [미로 탈출](https://github.com/JIWON1923/Algorithm/blob/master/DFS_BFS/maze_best.py)
---

## Sort
- 선택 정렬
    - 매번 작은 것을 선택하여 정렬하는 알고리즘
    - 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복하여 정렬하는 것이다.
    - 시간복잡도 O(N^2)
    
    
    ```python
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i] # swap
    
    print(array)
    ```
    
    
- 삽입 정렬
    - 데이터를 하나씩 확인해서 각 데이터를 적절한 위치에 삽입하자
    - 선택 정렬보다 실행 시간 측면에서 더 효율적이다.
    - 필요할 때에만 위치를 바꾸므로 **데이터가 거의 정렬되어 있을 때** 효율적이다.
    - 데이터가 적절한 위치에 들어가기 이전, 그 앞까지의 데이터는 이미 정렬되어있다고 가정한다. 정렬되어 있는 데이터 리스트에서 적절한 위치를 찾은 후 그 위치에 삽입된다.
    - 시간복잡도 O(N^2), 최선의 경우 O(N)
        
    
    ```python
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    for i in range(1, len(array)): # 첫번째 원소는 존재만으로 정렬되어있음을 가정
        for j in range(i, 0, -1) # i부터 첫번째까지 탐색
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break
    
    print(array)
    ```
    
    
- 퀵 정렬
    - 기준 데이터(pivot)을 설정하고, 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼다.
    - 시간복잡도 O(NlogN)
    
    
    ```python
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    
    def quick_sort(array):
        if len(array) <= 1: # 리스트가 하나 이하의 원소라면
            return array
            
        pivot = array[0]
        tail = array[1:] # 피벗을 제외한 리스트
        
        left_side = [x for x in tail if x <= pivot]
        right_side = [x for x in tail if x > pivot]
        
        return quick_sort(left_side) + [pivot] + quick_sort(right_side)
    
    print(quick_sort(array))
    ```
    
    
- 계수 정렬
    - **특정한 조건이 부합할 때**에만 사용할 수 있지만, 매우 빠른 정렬 알고리즘
    - 특정 조건: 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때
    - 일반적으로 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000을 넘지 않을 때 효과적으로 사용 가능하다.
    - 데이터의 값을 비교(비교 기반 정렬 알고리즘)하는 것이 아니라 별도의 리스트를 선언하여 정렬에 대한 정보를 담는다.
    - 시간복잡도 O(N + K), N: 데이터의 개수, K: 데이터 중 최댓값의 크기
    
    
    ```python
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    count = [0] * (max(array) + 1)
    
    for i in range(len(array)):
        count[array[i]] += 1
    
    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end = ' ')
    ```
    
   
- 예제
    - [위에서 아래로](https://github.com/JIWON1923/Algorithm/blob/master/Sort/Top_Down.py)
    - [성적이 낮은 순서로 학생 출력하기](https://github.com/JIWON1923/Algorithm/blob/master/Sort/InOrderOf_Score.py)
    - [두 배열의 원소 교체](https://github.com/JIWON1923/Algorithm/blob/master/Sort/Replacement_Array.py)
    
---
## Binary Search
- 순차 탐색
    - 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법이다.
    
    
    ```python
    def sequential_search(n, target, array):
        for i in range(n):
            if array[i] == target:
                return i + 1 #현재 위치 반한
    array = input().split()
    target = input()
    n = len(input_data)
    
    print(sequential_search(n, target, array))
    ```
    
    
- 이진 탐색
    - 배열 내부 데이터가 **정렬되어 있을 때** 사용 가능한 알고리즘이다.
    - 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 특징이 있다.
    - 시작점, 끝점, 중간점이라는 변수를 설정한다.
    - 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교하여 원하는 데이터를 찾는 과정이다.
    - 시간복잡도: O(logN), 한 번 확인할 때 마다 원소의 개수가 절반씩 줄어들기 때문
    
    
    
    - 재귀함수로 구현한 이진탐색
    
    
    ```python
    def binary_search(array, targer, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        
        if array[mid] == target:
            return mid
        
        elif array[mid] > target:
            return binary_search(array, target, start, mid-1)
        else:
            return binary_search(array, target, mid+1, end)
            
    n, target = list(map(int, input().split()))
    array = list(map(int, input().split()))
    
    result = binary_search(array, target, 0, n-1)
    
    if result == None:
        print("원소가 존재하지 않습니다.")
    else:
        print(result + 1)
    ```
    
    
    - 반복문으로 구현한 이진탐색
    
    
    ```python
    def binary_search(array, target, start, end):
        while start <= end:
            mid = (start + end) // 2
            if array[mid] == target:
                return mid
            elif array[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return None
    ```


- 트리 자료구조
    - 트리는 부모 노드와 자식 노드의 관계로 표현된다.
    - 트리의 최상단 노드를 루트 노드라고 한다.
    - 트리의 최하단 노드를 단말 노드라고 한다.
    - 트리에서 일부를 떼어내도 트리구조이며, 이를 서브트리라고 한다.
    - 트리는 파일 시스템과 같이 계층적이고, 정렬된 데이터를 다루기 적합하다.
    
- 이진 탐색 트리
    - 부모 노드보다 왼쪽 자식 노드가 작다
    - 부모 노드보다 오른쪽 자식 노드가 크다
    - 왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드
    
- 예제
    - [부품 찾기](https://github.com/JIWON1923/Algorithm/blob/master/Search/Practice2_findingPart.py)
    - [떡볶이 떡 만들기](https://github.com/JIWON1923/Algorithm/blob/master/Search/Practice3_CuttingRiceCake.py)
---

## Dynamic Programming

## Shortest Path

## Graph

---
## 기타
- 소수 찾기
    - math.sqrt를 사용하여 시간 복잡도 단축
- 에라토스테네스의 체
    - 여러 개의 수가 소수인지 아닌지 판별
    - O(NloglogN)
    - 메모리가 많이 필요하다.
    - 1,000,000이내로 주어지는 경우에 사용한다.
        - 이론상 400만 번 정도의 연산으로 해결 가능
    
    
    ```python
    def aritos(n):
        numbers = set(range(2, n+1))
        
        for i in range(numbers):
            if i in numbers:
                print(i)
                numbers -= set(range(2*i, n+1, i))
        return numbers
    ```
    
         
