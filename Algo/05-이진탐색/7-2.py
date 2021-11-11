array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

def binary_search(_arr, _target, _start, _end, _count):
    # 아예 못 찾을 때
    if _start > _end:
        print("찾지 못했습니다")
        return
    mid = (_start + _end) // 2

    if _arr[mid] == _target:
        print(mid, _count)
        return

    if _arr[mid] > _target:
        binary_search(_arr, _target, _start, mid - 1, _count + 1)
    else:
        binary_search(_arr, _target, mid + 1, _end, _count + 1)

binary_search(array, 4, 0, len(array) - 1, 1)