# 무게 순으로 볼링공을 고르고, 다음 사람이 공을 고른다.
# B가 선택하는 경우의 수는 점차 줄어든다.
# 무게 1인 볼링공 1개
# 무게 2인 볼링공: 2개
# 무게 3인 볼링공: 2개

# A가 무게 1 볼링공 선택 (1개) * B가 나머지 무게 볼링공 선택 (5 - 1개)
# B가 무게 2 볼링공 선택 (2개) * B가 나머지 무게 볼링공 선택 (4 - 2개)
# B가 무게 3 볼링공 선택 (2개) * B가 나머지 무게 볼링공 선택 (2 - 2개)

# n: 볼링공의 총 개수
n, m = map(int, input().split())
data = list(map(int, input().split()))

# 볼링공 최대 무게 10
# 무게 별 개수를 저장
arr = [0] * 11
for x in data:
    arr[x] += 1

result = 0
total_count = n
for i in range(1, 11):
    total_count -= arr[i]
    result += arr[i] * total_count

print(result)

#####################################################
# # 볼링공을 고르는 경우의 수
# 
# def solve(arr, idx, count, length):
#     global answer
#     if count == 2:
#         answer += 1
#         return
#     if length - idx < 2 - count:
#         return
# 
#     if len(arr) == 0 or (len(arr) == 1 and arr[0] != K[idx]):
#         solve(arr + [K[idx]], idx + 1, count + 1, length)
#     solve(arr, idx + 1, count, length)
# 
# 
# N, M = map(int, input().split())
# K = list(map(int, input().split()))
# 
# answer = 0
# solve([], 0, 0, N)
# print(answer)