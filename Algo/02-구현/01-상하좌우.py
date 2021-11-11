# (1, 1) ~ (N, N)까지
# 이동 명령에 따라 이동하여, 최종 도착지점의 좌표를 출력해라

def solution():
    n = int(input())
    directions = input().split()

    direction_dict = {
        "L": (0, -1),
        "R": (0, 1),
        "U": (-1, 0),
        "D": (1, 0)
    }

    current_pos = (1, 1)
    for d in directions:
        cr, cc = current_pos
        dr, dc = direction_dict[d]
        nr = cr + dr
        nc = cc + dc
        if 1 <= nr <= n and 1 <= nc <= n:
            current_pos = (nr, nc)
    print(current_pos[0], current_pos[1])

solution()