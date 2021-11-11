N, M = map(int, input().split())
CARDS = [list(map(int, input().split())) for _ in range(N)]

min_nums_by_row = []
for i in range(N):
    min_nums_by_row.append(min(CARDS[i]))

print(max(min_nums_by_row))