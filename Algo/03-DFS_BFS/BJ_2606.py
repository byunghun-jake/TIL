def dfs(graph, node, visited):
    global answer
    answer += 1
    visited[node] = True

    for n in graph[node]:
        if not visited[n]:
            dfs(graph, n, visited)


N = int(input())
E = int(input())
graph = [[] for _ in range(N + 1)]  # 1부터 시작

for _ in range(E):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)


visited = [False] * (N + 1)

answer = -1
dfs(graph, 1, visited)
print(answer)