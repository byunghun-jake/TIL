store = [0] * 100

def fibo(n):
    # print(f"fibo({n})", end=" ")
    if n == 1 or n == 2:
        return 1

    if not store[n]:
        store[n] = fibo(n - 1) + fibo(n - 2)
    return store[n]

print(fibo(99))

##################

store2 = [0] * 100
store2[1] = 1
store2[2] = 1

for n in range(3, 100):
    store2[n] = store2[n - 1] + store2[n - 2]

print(store2[99])