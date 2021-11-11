N, M, K = 5, 8, 3
NUMS = [2, 4, 5, 4, 6]
# N, M, K = 5, 7, 2
# NUMS = [3, 4, 3, 4, 3]

NUMS.sort(reverse=True)
answer = 0
for i in range(M):
    if i != 0 and i % K == 0:
        answer += NUMS[1]
    else:
        answer += NUMS[0]

print(answer)

#########################################
print(NUMS[1] * (M // (K + 1)) + NUMS[0] * (M - (M // (K + 1))))