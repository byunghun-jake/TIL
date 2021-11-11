# 4 5
# 00110
# 00011
# 11111
# 00000

from collections import deque

# N: Row length
# M: Column length
N, M = map(int, input().split())

board = []

for _ in range(N):
    board.append(list(map(int, list(input()))))

answer = 0

dr = [0, 1]
dc = [1, 0]

for r in range(N):
    for c in range(M):
        if board[r][c] == 0:
            answer += 1
            queue = deque()
            queue.append((r, c))
            while queue:
                cr, cc = queue.popleft()
                for i in range(2):
                    nr = cr + dr[i]
                    nc = cc + dc[i]
                    if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == 0:
                        queue.append((nr, nc))
                        board[nr][nc] = 1
print(answer)