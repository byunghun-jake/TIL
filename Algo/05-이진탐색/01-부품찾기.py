from sys import stdin

N = int(stdin.readline().strip())
store_parts = sorted(list(map(int, stdin.readline().strip().split())))
M = int(stdin.readline().strip())
need_parts = list(map(int, stdin.readline().strip().split()))

for i in range(M):
    start = 0
    end = len(store_parts) - 1
    target = need_parts[i]

    while start <= end:
        mid = (start + end) // 2

        if store_parts[mid] == target:
            print("yes", end=" ")
            break
        elif store_parts[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    else:
        print("no", end=" ")
