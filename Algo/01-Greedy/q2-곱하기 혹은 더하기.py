# 0 () 숫자 => +
# 1 () 숫자 => +
# 2 () 숫자 => *

# 두 숫자 중 0 또는 1이 있는 경우라면 더하기를 하는 것이 이득
# 없다면 곱하기를 하는 것이 이득이다.

N_LIST = list(map(int, list(input())))
answer = N_LIST[0]

for i in range(1, len(N_LIST)):
    if answer <= 1 or N_LIST[i] <= 1:
        answer += N_LIST[i]
    else:
        answer *= N_LIST[i]

print(answer)
