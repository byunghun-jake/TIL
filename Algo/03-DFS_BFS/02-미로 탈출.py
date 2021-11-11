# 최소 칸의 개수를 구하시오 => BFS

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

from collections import deque

N, M = map(int, input().split())
maze = [ list(map(int, list(input()))) for _ in range(N) ]
visited = [[-1 for _ in range(M)] for _ in range(N)]

sr, sc = 0, 0
er, ec = N, M

queue = deque()
queue.append((sr, sc))
visited[sr][sc] = 1

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

answer = -1

while queue and answer == -1:
    cr, cc = queue.popleft()
    count = visited[cr][cc]
    for i in range(4):
        nr = cr + dr[i]
        nc = cc + dc[i]
        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == -1:
            if nr == N - 1 and nc == M - 1:
                answer = count + 1
                break
            queue.append((nr, nc))
            visited[nr][nc] = count + 1

print(answer)