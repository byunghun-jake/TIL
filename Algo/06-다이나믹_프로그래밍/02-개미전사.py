# f(i) = i번째 창고에 도달할 때, 가지고 있는 식량의 최대 값
# box[i] = i번째 창고에 있는 식량
# f(i) = max(f(i - 1), f(i - 2) + box[i])

N = int(input())
containers = list(map(int, input().split()))

store = [0] * (N + 1)
store[1] = containers[0]
store[2] = containers[1]

for n in range(3, N + 1):
    store[n] = max(store[n - 1], store[n - 2] + containers[n - 1])

print(store[N])