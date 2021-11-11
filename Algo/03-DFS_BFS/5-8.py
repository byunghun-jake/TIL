def dfs(graph, v, visited):
    # 현재 노드 방문처리
    visited[v] = True
    print(v)

    # 인접 노드 탐색
    for adj_node in graph[v]:
        if not visited[adj_node]:
            dfs(graph, adj_node, visited)


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
dfs(graph, 1, visited)