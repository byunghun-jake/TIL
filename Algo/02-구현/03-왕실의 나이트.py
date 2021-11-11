# 나이트가 이동할 수 있는 방향은 총 8가지이다.

def solution():
    answer = 0
    pos = input()
    columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    r = int(pos[1]) - 1
    c = columns.index(pos[0])

    move_list = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]

    for move in move_list:
        nr = r + move[0]
        nc = c + move[1]
        print(nr, nc)
        if 0 <= nr < 8 and 0 <= nc < 8:
            answer += 1
    print(answer)

solution()