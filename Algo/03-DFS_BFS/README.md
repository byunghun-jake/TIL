# 탐색

많은 양의 데이터 중에서 원하는 데이터를 찾는 과정

대표적인 탐색 알고리즘으로 DFS와 BFS가 있다.

DFS와 BFS를 제대로 이해하려면 기본 자료구조인 스택과 큐에 대해 알아야 하며, 재귀 함수에 대해서도 알고 있어야 한다.



## 자료구조

데이터를 표현하고 관리하고 처리하기 위한 구조

스택과 큐는 자료구조의 기초 개념으로 다음의 두 핵심 함수로 구성된다.

- push: 데이터를 삽입(추가)한다.
- pop: 데이터를 삭제한다.

데이터를 삽입 / 삭제할 때에는 오버플로와 언더플로를 염두해두어야 한다.

- 오버플로: 데이터 저장공간이 꽉 찬 상태에서 데이터를 삽입할 때 발생한다.
- 언더플로: 데이터 저장공간이 비어있는 상태에서 데이터를 삭제하려고 할 때 발생한다.



### 스택

스택은 입구가 하나로, 먼저 넣은 데이터가 나중에 나오는 구조로 되어있다.

ex) 브라우저 히스토리

```python
stack = []
stack.append(1)	# 1
stack.append(2)	# 1 2
stack.append(3)	# 1 2 3
stack.append(4)	# 1 2 3 4
stack.pop()		# 1 2 3
stack.pop()		# 1 2
stack.pop()		# 1
stack.pop()		#
```

> 파이썬에서 스택을 구현할 때에는 별도의 라이브러리를 사용할 필요가 없다.

- List.append(data): 데이터를 삽입한다.
- List.pop(): 데이터를 삭제한다.



### 큐

큐는 두개의 입구로, 먼저 들어간 데이터가 먼저 나오는 구조로 되어있다.

ex) 대기열

```python
from collections import deque

queue = deque()

queue.append(1)	# 1
queue.append(2)	# 1 2
queue.append(3)	# 1 2 3
queue.popleft()	# 2 3
queue.popleft()	# 3
queue.popleft()	# 
```

> 파이썬으로 Queue를 구현할 때에는 collections 모듈에 있는 deque 자료구조를 활용하자.



### 재귀 함수

자기 자신을 다시 호출하는 함수

#### 재귀 함수의 종료 조건

재귀 함수를 문제에서 사용할 때에는 재귀 함수가 언제 끝날지, **종료 조건을 꼭 명시해야 한다.**

```python
def recursive_function(i):
    if i == 10:
        return
    print('재귀 호출!')
    recursive_function(i + 1)
```

재귀 함수는 내부적으로 스택 자료구조와 동일하다. 따라서, 스택 자료구조를 사용해야 하는 상당수 알고리즘은 재귀 함수를 이용해서 구현할 수 있다.
ex) DFS

```python
# 팩토리얼
def factorial_iterative(n):
    answer = 1
    for i in range(2, n + 1):
        answer *= i
	return answer

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)
```



## 탐색 알고리즘 DFS / BFS

### DFS

Depth first search

깊이 우선 탐색이라고도 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다.

#### 그래프

그래프는 노드(Node)와 간선(Edge)으로 표현되며, 이때 노드를 정점(Vertex)라고도 말한다.

그래프 탐색이란, 하나의 노드에서 시작하여 여러 노드를 탐색하는 것을 말한다.

두 노드가 간선으로 연결되어 있으면, '두 노드는 인접하다(Adjacent)'라고 표현한다.

프로그래밍에서 그래프를 표현하는 방식은 크게 2가지가 있다.

##### 1. 인접 행렬(Adjacency Matrix)

> 2차원 배열로 그래프의 연결 관계를 표현하는 방식

연결되어 있는 노드끼리 연결된 간선의 가중치가 존재할 때, 연결되어 있지 않은 노드끼리는 무한의 비용이라고 작성한다.

```python
# 0 - (7) - 1
# 0 - (5) - 2

INF = 987654321
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]
```



##### 2. 인접 리스트(Adjacency List)

> 리스트로 연결 관계를 표현하는 방식

```python
# 0 - (7) - 1
# 0 - (5) - 2

# 노드의 개수 == 행의 개수
graph = [[] for _ in range(3)]

# 0번 노드와 연결된 노드를 저장한다. (노드 번호, 간선 가중치)
graph[0].append((1, 7))
graph[0].append((2, 5))

# 1번 노드와 연결된 노드를 저장한다.
graph[1].append((0, 7))

# 2번 노드와 연결된 노드를 저장한다.
graph[2].append((0, 5))

graph	# [[(1, 7), (2, 5)], [(0, 7)], [(0, 5)]]
```



##### 두 방식의 차이

- 메모리 측면

  인접 행렬 방식은 모든 관계를 저장하므로, 노드의 개수가 많을 수록 불필요하게 차지하는 메모리가 늘어난다.

  인접 리스트 방식은 연결된 관계만 저장하기 때문에 메모리를 효율적으로 사용한다.

- 속도 측면

  인접 행렬 방식은 특정한 두 노드가 연결되어있는지 바로 확인할 수 있다.

  인접 리스트 방식은 연결된 데이터를 하나하나 확인해야 하기 때문에 속도가 느리다.



DFS는 특정한 경로로 가능한 깊숙이 노드들을 탐색한 후, 더 이상 탐색할 수 없게 되면 다시 돌아가 다른 경로로 탐색하는 알고리즘이다.

#### 동작 과정

```python
# 1. 탐색 시작 노드를 스택에 삽입하고, 해당 노드를 방문처리
stack.append(Node)
visited[Node] = True

# 2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면, 그 인접 노드를 스택에 넣고 방문처리를 한다.
# 방문하지 않은 인접노드가 없으면, 스택에서 최상단 노드를 꺼낸다.
Node = stack[-1]
for n in graph[Node]:
    if visited[n] == False:
        stack.append(n)
        visited[n] = True
        break
else:
    stack.pop()

# 3. 2번 과정을 더 이상 수행할 수 없을 때까지 반복한다.
```



```python
graph = [
    # ...
]
visited = [False] * N	# N: 노드 개수

s = 1
stack.append(s)

while stack:
    node = stack[-1]
    for n in graph[node]:
        if not visited[n]:
            stack.append(n)
            visited[n] = True
            break
	else:
        stack.pop()
```



```python
def dfs(graph, node, visited):
    visited[node] = True
    print(node, end=' ')
    
    for n in graph[node]:
        if not visited[n]:
            dfs(graph, n, visited)

visited = [False] * N	# N: 노드 개수
dfs(graph, 1, visited)
```



### BFS

가까운 노드부터 탐색하는 알고리즘

#### 동작 과정

```python
from collections import deque
queue = deque()
# 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
queue.append(s)
visited[s] = True

# 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
node = queue.popleft()
for n in graph[node]:
    if not visited[n]:
        queue.append(n)
        visited[n]

# 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.
```



### 문제

- [x] BJ_2606 바이러스
- [x] Book_음료수 얼려 먹기
- [x] Book_미로 탈출
- [x] BJ_11724 연결 요소의 개수









