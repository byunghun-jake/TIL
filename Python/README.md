# Numpy

Numerial Python

Python에서 대규모 다차원 배열을 다룰 수 있게 도와주는 라이브러리

Python 대표적인 라이브러리

1. Pandas
2. Numpy
3. Matplotlib



## Why?

데이터의 대부분은 숫자 배열로 볼 수 있다. (다룰 수 있다)

반복문 없이 배열 처리 가능!

파이썬 리스트에 비해, 빠른 연산을 지원하고 메모리를 효율적으로 사용한다.



## Python List vs Numpy

### Python List

```python
list_arr = list(range(5))
print(list_arr)       # [0, 1, 2, 3, 4] => 쉼표로 구분
print(type(list_arr)) # <class 'list'>
```

### Numpy

```python
import numpy as np
np_arr = np.array(range(5))
print(np_arr)       # [0 1 2 3 4] => 띄어쓰기로 구분
print(type(np_arr)) # <class 'numpy.ndarray'>
```

- ndarray란?

  n차원의 array



## 배열의 기초



### 배열의 데이터 타입 `dtype`

파이썬 리스트와 달리 같은 데이터 타입만 저장할 수 있다.

```python
import numpy as np

arr = np.array([0, 1, 2, 3, 4], dtype=float)
print(arr) # [0. 1. 2. 3. 4.]
print(arr.dtype) # "float64"
print(arr.astype(int)) # [0 1 2 3 4]
```

- `int` 정수형 타입
- `float` 실수형 타입
- `str` 문자열 타입
- `bool` 부울 타입

### 배열의 속성

`ndarray` 의 차원 관련 속성

- `ndim`: n + dimension (N차원)
- `shape`: 모양

```python
arr = np.array([0, 1, 2, 3])
print(arr.ndim) # 1
print(arr.shape) # (4,)

arr2 = np.array([[0, 1, 2], [3, 4, 5]])
print(arr.ndim) # 2
print(arr.shape) # (2, 3)
print(arr.size) # 6
print(len(arr)) # 2
```

## Indexing & Slicing

### Indexing

인덱스로 값을 찾기

```python
x = np.arange(7)

print(x) # [0 1 2 3 4 5 6]
print(x[3]) # 3
print(x[7]) # 아무것도 출력되지 않음
# IndexError: index 7 is out of bounds

x[0] = 10
print(x) # [10 1 2 3 4 5 6]
x = np.arange(1, 13, 1) # 1 ~ 12까지 1씩 증가
x.shape = 3, 4          # 3 X 4 행렬로 변환
print(x)
# [[1 2 3 4],
#  [5 6 7 8],
#  [9 10 11 12]]

print(x[2, 3]) # 12
```