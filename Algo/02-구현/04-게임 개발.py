# 현재 방향을 기준으로 왼쪽방향부터 갈 곳을 정한다.
    # 가보지 않은 칸이라면, 해당 칸으로 전진
    # 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전
# 네 방향 모두 이미 가봤거나, 바다로 되어 있다면, 바라보는 방향을 유지한 채로 한칸 뒤로 간다.

def solution():
    d_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    n, m = map(int, input().split())
    cr, cc, cd = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    visited[cr][cc] = 1

    answer = 1
    on_game = True
    cant_go_count = 0
    while on_game:
        # 1. 왼쪽 방향에 갈 수 있는지 확인한다.
        nd = (cd - 1) % 4
        nr = cr + d_list[nd][0]
        nc = cc + d_list[nd][1]
        if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == 0 and visited[nr][nc] == 0:
            # 왼쪽 방향으로 갈 수 있다면
            cant_go_count = 0
            cr = nr
            cc = nc
            cd = nd
            answer += 1
            visited[cr][cc] = 1
        else:
            # 왼쪽 방향으로 갈 수 없다면
            if cant_go_count == 4:
                # 네 방향 모두 갈 수 없다면,
                nd = (cd - 2) % 4
                nr = cr + d_list[nd][0]
                nc = cc + d_list[nd][1]
                if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == 1:
                    # 뒤에도 바다라면?
                    on_game = False
                else:
                    cr = nr
                    cc = nc
                    cant_go_count = 0
            else:
                cant_go_count += 1
                cd = nd
    print(answer)


solution()