N = 1260

answer = 0

# if N >= 500:
#     tmp = N // 500
#     answer += tmp
#     N -= tmp * 500
# if N >= 100:
#     tmp = N // 100
#     answer += tmp
#     N -= tmp * 100
# if N >= 50:
#     tmp = N // 50
#     answer += tmp
#     N -= tmp * 50
# if N >= 10:
#     tmp = N // 10
#     answer += tmp

coin_list = [500, 100, 50, 10]
for coin in coin_list:
    answer += N // coin
    N %= coin

print(answer)
