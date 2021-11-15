N = int(input())
coin_list = list(map(int, input().split()))
coin_list.sort()

# 가장 작은 수부터 하나씩 더해간다.
# 만들 수 없을 것 같은 수를 정한다. (target)
answer = -1
target = 1
for coin in coin_list:
    if target < coin:
        answer = target
        break
    else:
        target += coin

print(answer)

#######################################################################################################################
# 1. 가지고 있는 동전 중 가장 적은 금액의 동전이 1보다 크다면, 최소 금액의 동전보다 1 작은 금액이 결과값이 된다.
# 2. 동전으로 만들 수 있는 모든 금액을 만들고, 배열에 저장한다. 저장한 배열을 탐색하고, 빈 값을 갖는 배열의 인덱스를 결과값으로 한다.

# def solve(arr, idx, length):
#     global price_list
#     if idx == length:
#         price_list[sum(arr)] = 1
#         return
#
#     solve(arr + [coin_list[idx]], idx + 1, length)
#     solve(arr, idx + 1, length)
#
# N = int(input())
# coin_list = list(map(int, input().split()))
# coin_list.sort()
# total = sum(coin_list)
#
# price_list = [0] * (total + 1)
#
# solve([], 0, N)
#
# for i in range(total):
#     if price_list[i] == 0:
#         print(i)

