N, K = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

sorted_a = sorted(arr_a)
sorted_b = sorted(arr_b, reverse=True)

for i in range(K):
    a_min = sorted_a[i]
    b_max = sorted_b[i]
    if a_min < b_max:
        sorted_a[i], sorted_b[i] = sorted_b[i], sorted_a[i]
    else:
        break

print(sorted_a)
print(sum(sorted_a))
