# N = 가로길이
# f(N) = 가로 길이가 N인 바닥을 덮개로 덮을 수 있는 경우의 수
# f(1) = 1
# f(2) = 3

# f(n) = f(n-1) + (f(n-2) * 2)

N = int(input())

store = [0] * (N + 1)
store[1] = 1
store[2] = 3

for n in range(3, N + 1):
    store[n] = store[n - 1] + (store[n - 2] * 2)

print(store[N])