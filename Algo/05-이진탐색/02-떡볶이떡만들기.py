import sys

N, M = map(int, sys.stdin.readline().strip().split())

rice_cake_list = list(map(int, sys.stdin.readline().strip().split()))

start = 0
end = max(rice_cake_list)

while start <= end:
    mid = (start + end) // 2

    total = 0
    for rice_cake in rice_cake_list:
        if rice_cake <= mid: continue

        total += rice_cake - mid

    if M == total:
        print(mid)
        break
    elif M > total:
        end = mid - 1
    else:
        start = mid + 1

