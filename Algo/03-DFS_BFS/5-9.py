from collections import deque

def bfs(graph, v, visited):
    q = deque()
    q.append(v)
    visited[v] = True

    while q:
        node = q.popleft()
        print(node)
        for adj_node in graph[node]:
            if not visited[adj_node]:
                visited[adj_node] = True
                q.append(adj_node)
        

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

visited = [False] * 9
bfs(graph, 1, visited)