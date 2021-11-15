import sys

N, M = map(int, sys.stdin.readline().strip().split())

won_list = list(map(int, sys.stdin.readline().strip().split()))

# 적은 금액부터 큰 금액까지 확인하면서 차례대로 만들 수 있는 화폐 개수를 찾는다.
# a_(i-k)가 있다면,
    # a_(i) = min(a_(i), a_(i-k))
# a_(i-k)가 없다면,
    # a_(i) = 10,001

# 초기화
count_list = [10001 for _ in range(M + 1)]
count_list[0] = 0

# 화폐 단위 순서대로 확인
for won in won_list:
    i = won
    while i <= M:
        count_list[i] = min(count_list[i-won] + 1, count_list[i])
        i += 1

print(count_list[M])