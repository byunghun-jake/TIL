array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

start = 0
end = len(array) - 1
target = 4
answer = None

while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
        answer = mid
        break
    elif array[mid] > target:
        end = mid - 1
    else:
        start = mid + 1

print(answer)