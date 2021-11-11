from collections import deque
import sys

def bfs(_graph, start, _visited):
    queue = deque([start])
    _visited[start] = True

    while queue:
        _node = queue.popleft()
        for n in _graph[_node]:
            if not _visited[n]:
                _visited[n] = True
                queue.append(n)



N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().strip().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

answer = 0

for i in range(1, N + 1):
    if visited[i]: continue
    answer += 1
    bfs(graph, i, visited)

print(answer)