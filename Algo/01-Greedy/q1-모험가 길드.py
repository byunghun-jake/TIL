# 여행을 떠날 수 있는 그룹 수의 최대값
# 공포도를 오름차순으로 정렬한다.
# 작게 그룹을 구성할 수 있는 대로 여행을 떠나면 된다.

N = int(input())
H_LIST = list(map(int, input().split()))
H_LIST.sort()

answer = 0

group = []
for H in H_LIST:
    group.append(H)
    if len(group) >= max(group):
        group = []
        answer += 1

print(answer)

