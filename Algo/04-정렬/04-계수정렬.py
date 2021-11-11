array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

answer = []
max_num = max(array)

counting_arr = [0] * (max_num + 1)

for num in array:
    counting_arr[num] += 1

for i in range(len(counting_arr)):
    for j in range(counting_arr[i]):
        answer.append(i)
print(answer)
