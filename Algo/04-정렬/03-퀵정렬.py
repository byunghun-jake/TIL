array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr, start, end):
    # 종료 조건
    if start >= end:
        return
    pivot_idx = start
    L = start + 1
    R = end
    while L <= R:
        # L: pivot보다 큰 값을 찾는다
        while L <= end and array[L] <= array[pivot_idx]:
            L += 1
        # R: pivot보다 작은 값을 찾는다
        while R > start and array[R] >= array[pivot_idx]:
            R -= 1
        # L과 R이 엇갈린 경우
        if L > R:
            array[R], array[pivot_idx] = array[pivot_idx], array[R]
        else:
            array[R], array[L] = array[L], array[R]
    # pivot을 기준으로 두 영역으로 나누어 정렬 시작
    quick_sort(arr, start, R - 1)
    quick_sort(arr, R + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)