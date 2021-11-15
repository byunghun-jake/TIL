S = list(map(int, list(input())))

# 모두 0으로 뒤집는 경우
# 모두 1로 뒤집는 경우
count0 = 0
count1 = 0

# 첫 번째 문자
if S[0] == 0:
    count1 += 1
else:
    count0 += 1

# 문자가 바뀌는 경우 확인
# 0 => 1로
# 1 => 0으로

for i in range(len(S) - 1):
    if S[i] != S[i + 1]:
        if S[i + 1] == 0:
            count1 += 1
        else:
            count0 += 1

print(min(count0, count1))