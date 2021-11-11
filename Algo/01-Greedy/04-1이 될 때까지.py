# P.99

# 1. N이 K로 나누어 떨어지는지 확인한다.
# 2. N이 K로 나누어 떨어진다면, K로 나누고 몫을 N으로 한다.
# 3. N이 K로 나누어 떨어지지 않는다면, N을 1로 뺀 후 다시 1번으로 돌아간다.

N, K = map(int, input().split())

answer = 0

while N != 1:
    if N % K == 0:
        answer += 1
        N //= K
    else:
        answer += 1
        N -= 1

print(answer)