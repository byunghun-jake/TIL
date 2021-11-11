# if x % 5 == 0 => x / 5
# if x % 3 == 0 => x / 3
# if x % 2 == 0 => x / 2
# x - 1
import sys

x = int(sys.stdin.readline().strip())

store = [-1] * (x + 1)
# 각 인덱스에 해당하는 숫자에서 1까지 도달하는 데 걸리는 최소 횟수
store[1] = 0
store[2] = 1

# f(x) = f(x - 1) * 5
# f(x) = f(x - 1) * 3
# f(x) = f(x - 1) * 2
# f(x) = f(x - 1) + 1

# for n in range(1, x + 1):
#     if (n + 1) <= x:
#         if store[n + 1] == -1:
#             store[n + 1] = store[n] + 1
#         else:
#             store[n + 1] = min(store[n + 1], store[n] + 1)
#     if (n * 5) <= x:
#         if store[n * 5] == -1:
#             store[n * 5] = store[n] + 1
#         else:
#             store[n * 5] = min(store[n * 5], store[n] + 1)
#     if (n * 3) <= x:
#         if store[n * 3] == -1:
#             store[n * 3] = store[n] + 1
#         else:
#             store[n * 3] = min(store[n * 3], store[n] + 1)
#     if (n * 2) <= x:
#         if store[n * 2] == -1:
#             store[n * 2] = store[n] + 1
#         else:
#             store[n * 2] = min(store[n * 2], store[n] + 1)
#
# print(store[x])

for n in range(2, x + 1):
    # 1보다 작은 수에서 1만큼 더해서 만들 수 있음
    store[n] = store[n - 1] + 1
    if n % 2 == 0:
        store[n] = min(store[n], store[n // 2] + 1)
    if n % 3 == 0:
        store[n] = min(store[n], store[n // 3] + 1)
    if n % 5 == 0:
        store[n] = min(store[n], store[n // 5] + 1)
print(store[x])