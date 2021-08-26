### 백준 - 5430 (AC)

[큐덱 - AC](https://www.acmicpc.net/problem/5430)

#### 내 코드 (성능 🤣)

```python
import sys

TC = int(sys.stdin.readline().strip())

for tc in range(TC):
    operations = sys.stdin.readline().strip()
    N = int(sys.stdin.readline().strip())
    NUMS = sys.stdin.readline().strip()[1:-1]
    direction = True
    if len(NUMS) < 1:
        num_list = []
    else:
        num_list = list(map(int, NUMS.split(",")))
    for operation in operations:
        if operation == "R":
            direction = not direction
        elif operation == "D":
            if len(num_list) < 1:
                print("error")
                break
            if direction:
                num_list.pop(0)
            else:
                num_list.pop()
    else:
        if not direction:
            num_list = num_list[::-1]
        print(f"[{','.join(list(map(str, num_list)))}]")
```



#### 다른 분 코드 참고 (성능 😍)

```python
for tc in range(TC):
    operations = sys.stdin.readline().strip()
    N = int(sys.stdin.readline().strip())
    NUMS = sys.stdin.readline().strip()[1:-1].split(",")
    is_front_pop = True
    start_idx = 0
    end_idx = N
    for operation in operations:
        if operation == "R":
            is_front_pop = not is_front_pop
        else:
            if end_idx <= start_idx:
                print("error")
                break
            if is_front_pop:
                start_idx += 1
            else:
                end_idx -= 1
    else:
        answer = NUMS[start_idx:end_idx]
        if not is_front_pop:
            answer = answer[::-1]

        print(f"[{','.join(answer)}]")
```



**성능 차이**

> Why?
>
> 내가 처음에 짠 코드는 매번 배열의 길이에 변화를 주는, 특히 pop(0)과 같이 시간이 오래걸리는 연산을 했기 때문이다.
>
> 배열의 양쪽 끝에 변화가 생긴다면, 양 끝 인덱스를 조작하는 것으로 대체할 수 있다는 생각을 해야겠다.

![image-20210707192813558](README.assets/image-20210707192813558.png)





### 백준 - 2630 (색종이 만들기)

[링크](https://www.acmicpc.net/problem/2630)

#### 이론

- 쿼드트리





#### 내 코드

```python
# 2중 반복문을 
def check_board_color(r, c, n):
    color = BOARD[r][c]
    for i in range(r, r + n):
        for j in range(c, c + n):
            if color != BOARD[i][j]:
                return False
    return True


def solve(r, c, n):
    # board 탐색
    if check_board_color(r, c, n):
        # 해당하는 색 카운팅
        color = BOARD[r][c]
        paper_count[color] += 1
    else:
        # 4개로 분할한 뒤 재귀호출
        mid = n // 2
        # 2사분면
        solve(r, c, mid)
        # 1사분면
        solve(r + mid, c, mid)
        # 3사분면
        solve(r, c + mid, mid)
        # 4사분면
        solve(r + mid, c + mid, mid)


N = int(input())
BOARD = [list(map(int, input().split())) for _ in range(N)]
paper_count = [0, 0]

solve(0, 0, N)
print(paper_count[0])
print(paper_count[1])
```



### 백준 2667 단지번호붙이기



#### 내 코드

```python
# 1. 1의 값을 찾는 과정
# 2. 1을 찾았을 때, 해당 지점을 방문한 적이 있었는지 확인
# 3. 방문한 적이 있었다면 넘어간다.
# 4. 방문한 적이 없었다면 그 위치를 기준으로 4방향으로 탐색을 진행한다.
# 5. 탐색이 끝났다면 단지의 크기를 저장한다.
# 6. 단지 인덱스를 1 크게 해준 뒤, 다시 1번으로 돌아간다.

# N: 지도의 크기 (~25)
N = int(input())
MAP = [list(map(int, list(input()))) for _ in range(N)]
visited = [[False] * N for _ in range(N)]


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(sr, sc):
    count = 1
    queue = [(sr, sc)]
    visited[sr][sc] = True

    while queue:
        snr, snc = queue[0]
        for i in range(4):
            nnr = snr + dr[i]
            nnc = snc + dc[i]
            if 0 <= nnr < N and 0 <= nnc < N:
                if MAP[nnr][nnc] and not visited[nnr][nnc]:
                    queue.append((nnr, nnc))
                    count += 1
                    visited[nnr][nnc] = True
        else:
            queue.pop(0)
    return count


count_list = []

for r in range(N):
    for c in range(N):
        if MAP[r][c] and not visited[r][c]:
            count_list.append(bfs(r, c))

print(len(count_list))
for count in sorted(count_list):
    print(count)
```





#### 다른 사람 코드

- 인덱스 범위를 넘어가는 지 확인하는 부분에서 `ny in range(N)`과 같이 `in` 연산자와 `range()`를 사용했다.

- BFS를 구현하기 위해 deque를 사용했다.

  `queue.pop(0) === dq.popleft()`

```python
from collections import deque

N = int(input())
map_arr = [list(input()) for _ in range(N)]

def bfs(y, x, cnt):
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    dq = deque([(y, x)])
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny in range(N) and nx in range(N) and map_arr[ny][nx] == '1':
                map_arr[ny][nx] = '0'
                dq.append((ny, nx))
                cnt += 1
    return cnt

answer = []
for y in range(N):
    for x in range(N):
        if map_arr[y][x] == '1':
            map_arr[y][x] = '0'
            result = bfs(y, x, 1)
            answer.append(result)

print(len(answer))
for i in sorted(answer):
    print(i)
```





### 1012_유기농 배추

```python
# 지렁이의 이동 범위는 기준 위치에서 상하좌우
# 배추를 지키기 위해 필요한 최소 지렁이의 마리수를 구해라
# 배추 군집의 개수를 구하면 된다.

import sys
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(sr, sc):
    dq = deque([(sr, sc)])
    visited[sr][sc] = 1

    while dq:
        cr, cc = dq.popleft()

        for di in range(4):
            nr = cr + dr[di]
            nc = cc + dc[di]
            if nr in range(N) and nc in range(M):
                if MAP[nr][nc] and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    dq.append((nr, nc))


# T: 테스트 케이스
T = int(input())

for tc in range(T):
    # M: 가로 길이 (~50)
    # N: 세로 길이 (~50)
    # K: 배추의 개수 (~2500)
    M, N, K = map(int, input().split())

    answer = 0

    MAP = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    for _ in range(K):
        c, r = map(int, sys.stdin.readline().strip().split())
        MAP[r][c] = 1

    for r in range(N):
        for c in range(M):
            if MAP[r][c] and not visited[r][c]:
                bfs(r, c)
                answer += 1

    print(answer)
```



#### 다른 사람 코드

- 재귀로 넘겨줄 때, 인자를 바꿔서 보내주는 방식이 인상적

```python
import sys
sys.setrecursionlimit(3000)

def dfs(i, j, N, M, np):
    if i < 0 or j >= N or i >= M or j < 0 or np[i][j] == 0: return
    np[i][j] = 0
    dfs(i + 1, j, N, M, np)
    dfs(i, j + 1, N, M, np)
    dfs(i - 1, j, N, M, np)
    dfs(i, j - 1, N, M, np)

T = int(sys.stdin.readline())
for i in range(T):
    N, M, K = map(int, sys.stdin.readline().split()); earthworm = 0
    Napa = [[0] * N for _ in range(M)]
    for j in range(K):
        x, y = map(int, sys.stdin.readline().split())
        Napa[y][x] = True
    for x in range(M):
        for y in range(N):
            if Napa[x][y] == True:
                dfs(x,y,N,M,Napa); earthworm += 1
    print(earthworm)
```





### 2178_미로탐색



### 7576_토마토

#### 내 코드 - 2

- 모든 행/열을 탐색하는 것은 비효율적이라고 생각
- 처음 행/열을 탐색할 때, 익지 않은 토마토의 개수를 따로 저장하여 bfs 탐색 시 상태가 변화하였을 때 1씩 차감하여 남은 토마토의 개수를 확인할 수 있을 것





#### 내 코드 - 1

- 모든 행, 열을 탐색하여 익은 토마토의 위치를 저장
- 익은 토마토의 위치를 가지고 bfs 탐색
- 방문기록을 남기는 대신 익지 않은 토마토에서 익은 토마토로 값을 직접 변경 (0 => 1)

- 탐색이 종료된 뒤, 모든 행/열을 탐색하여 안익은 토마토가 있는지 확인

```python
from collections import deque


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs():
    result = 0
    while dq:
        cr, cc, day = dq.popleft()
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if nr in range(R) and nc in range(C) and MAP[nr][nc] == 0:
                dq.append((nr, nc, day + 1))
                MAP[nr][nc] = 1
                result = day + 1

    return result



C, R = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(R)]
# 직접 값을 바꿔보자

dq = deque([])

for r in range(R):
    for c in range(C):
        if MAP[r][c] == 1:
            dq.append((r, c, 0))

answer = bfs()

for r in range(R):
    for c in range(C):
        if MAP[r][c] == 0:
            answer = -1

print(answer)
```



### 7562_나이트의 이동

> 유효성 검사를 할 때, `range`를 사용하는 경우 시간초과가 발생하는 케이스

#### 하이라이트

```python
if 0 <= nr < L and 0 <= nc < L and not visited[nr][nc]:
	# 통과

if nr in range(L) and nc in range(L) and not visited[nr][nc]:
    # 시간초과
```



#### 내 코드

```python
# BFS
# 1. 8개 방향으로 이동
# 2. 방문 기록
# 3. queue 에 저장
# 몇 번만에 이동했는지 출력해야 한다.
from collections import deque

dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(r, c):
    global er, ec
    dq = deque([(r, c, 0)])
    visited[r][c] = True

    while dq:
        cr, cc, count = dq.popleft()
        # 도착했는지 확인
        if cr == er and cc == ec:
            return count

        # 8개 방향 탐색
        for i in range(8):
            nr = cr + dr[i]
            nc = cc + dc[i]
            # range는 시간이 많이 걸린다.
            # if nr in range(L) and nc in range(L) and not visited[nr][nc]:
            if 0 <= nr < L and 0 <= nc < L and not visited[nr][nc]:
                if cr == er and cc == ec:
                    return count
                dq.append((nr, nc, count + 1))
                visited[nr][nc] = True


TC = int(input())
for tc in range(TC):
    L = int(input())
    sr, sc = list(map(int, input().split()))
    er, ec = map(int, input().split())
    visited = [[False] * L for _ in range(L)]
    answer = bfs(sr, sc)
    print(answer)
```



### 1707_이분그래프

#### 하이라이트

- 이분그래프란?

  > 인접한 노드 끼리 같은 그룹에 해당하지 않는 그래프

  ![img](https://media.vlpt.us/images/i-zro/post/2e66bcb7-05f8-45e0-a794-a272eb508d06/image.png)

- 메모리초과 발생

  N1과 N2가 연결되어 있을 때, `board[N1][N2] = board[N2][N1] = True`와 같이 저장하였더니 메모리를 초과해버렸다.

  이차원 배열을 만들었기 때문에 생긴 일 같은데, 배열의 크기는 다음과 같다.

  `V(1 <= V <= 20,000)`

  2만개 이상 넘어가는 경우에는 메모리초과에 주의해야겠다.

  ---

  해결책:

  `[[], [], [], ...]`1차원 배열을 만들어, 해당하는 index에 연결된 노드 번호를 추가해주는 방식으로 진행했다.

  

- 시간초과 발생

  어디에서 시간을 줄여야 할까?

  - 다음 그룹을 지정할 때, 나머지 연산을 수행하는 데, 여기에서 시간이 오래 걸리는 걸까?

    그룹을 -1과 1로 나누어 배정하는 것으로 변경해보자.

    > 해결하지 못했다.

  - 갈 수 있는지 확인하는 부분을 다르게 생각해보자.

    n1 이라는 노드에서 모든 노드를 탐색하며 갈 수 있는지 없는지 확인하는 것 보단, 앞서 저장해 두었던, 연결된 노드를 저장한 리스트를 활용하는 것이 효율적일 것이라는 생각이 든다.

    ```python
    # 이전
    for nn in range(1, node_count + 1):
        if nn not in board[cn]:
            continue
    ```

    ```python
    # 이후
    for nn in board[cn]:
    ```

  

- 틀렸습니다

  아예 연결이 끊긴 노드가 있을 수 있다는 것을 고려하지 않았다.

  모든 노드를 시작점으로 탐색을 수행해야 하며, 만일 1이 아닌 노드에서 다시 탐색을 수행할 수 있다면 그 그래프는 이분탐색 그래프일 수 없을 것

  ```python
  # 이전
  bfs(1)
  ```

  ```python
  # 이후
  for sn in range(1, node_count + 1):
      if not visited[sn]:
          answer = bfs(sn)
          if answer == "NO":
              break
  ```

  

#### 내 코드 - 정답

```python
# 인접한 정점들과는 다른 그룹에 속하는지 확인
import sys
from collections import deque


def bfs(sn):
    dq = deque([sn])
    visited[sn] = 1

    while dq:
        cn = dq.popleft()
        for nn in board[cn]:
            # 그룹 확인
            if visited[nn] == 0:
                dq.append(nn)
                visited[nn] = -visited[cn]
            elif visited[nn] == visited[cn]:
                return "NO"
    return "YES"



TC = int(input())
for tc in range(TC):
    node_count, line_count = map(int, input().split())
    board = [[] for _ in range(node_count + 1)]
    visited = [0] * (node_count + 1)

    for _ in range(line_count):
        r, c = map(int, sys.stdin.readline().strip().split())
        board[r].append(c)
        board[c].append(r)

    answer = ""
    for sn in range(1, node_count + 1):
        if not visited[sn]:
            answer = bfs(sn)
            if answer == "NO":
                break
    print(answer)
```





#### 내 코드 - 시간초과

```python
# 인접한 정점들과는 다른 그룹에 속하는지 확인
import sys
from collections import deque


def bfs(sn):
    dq = deque([(sn, 1)])
    group[sn] = 1

    while dq:
        cn, t = dq.popleft()
        for nn in range(1, node_count + 1):
            # 갈 수 있는지 확인
            if nn not in board[cn]:
                continue
            # 그룹 확인
            if group[nn] == 0:
                dq.append((nn, t * (-1)))
                group[nn] = t * (-1)
            elif group[nn] == t:
                return "NO"
    return "YES"



TC = int(input())
for tc in range(TC):
    node_count, line_count = map(int, input().split())
    board = [[] for _ in range(node_count + 1)]
    group = [0] * (node_count + 1)

    for _ in range(line_count):
        r, c = map(int, sys.stdin.readline().strip().split())
        board[r].append(c)
        board[c].append(r)

    print(bfs(1))
```







#### 현재 코드

```python
import sys

sys.stdin = open("1210_Ladder1.txt")
# 어느 사다리를 고르면 X표시에 도착하게 될까?

# X 표시에서 거꾸로 올라가는 것으로 전환해보자
# 가로선을 만났을 떄 어떻게 동작해야 할까?
    # 위로 올라가던 중 좌 or 우에 있는 가로선을 만나면, 그 가로선으로 이동한다.
    # 현재 위치에서 좌, 우를 탐색한 뒤
        # 있으면 해당 가로선으로 이동
        # 없으면 위 칸으로 이동
    
    # 좌 or 우로 이동하던 중 위로 갈 수 있는 길을 만나면, 위로 올라간다.

N = 100

for _ in range(1, 11):
    tc = int(input())
    ladder_map = []
    for _ in range(N):
        row = list(map(int, sys.stdin.readline().strip().split()))
        ladder_map.append(row)

    # X 위치를 찾는다.
    start_col = 0
    for idx in range(N):
        if ladder_map[N - 1][idx] == 2:
            start_col = idx
            break

    # X 위치를 시작지점으로 탐색을 시작한다.
    cr = N - 1
    cc = start_col
    c_direction = 0

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    while cr != 0:
        # 좌
        if cc > 1 and ladder_map[cr][cc - 1] == 1:
            while cc > 0 and ladder_map[cr][cc - 1] == 1:
                cc -= 1
            else:
                cr -= 1
                continue
        # 우
        if cc < 99 and ladder_map[cr][cc + 1] == 1:
            while cc < 99 and ladder_map[cr][cc + 1] == 1:
                cc += 1
            else:
                cr -= 1
                continue
        # 양쪽 다 없을 때
        cr -= 1
        cc = cc
    print(f"#{tc} {cc}")
```





#### 과거 코드

```python
N = 100

for _ in range(10):
    # 1. test_case 번호 입력
    tc = int(input())

    # 2. 100x100 배열 입력
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    # 3. [99, 0] 부터 오른쪽으로 이동하며, 2의 위치 찾기
    r = N - 1
    c = 0
    for c_idx in range(N):
        if arr[r][c_idx] == 2:
            c = c_idx
            break
    
    # 4. 도착점부터 위로 올라가며, 작업 수행
    while r > 0:
        # 4-1. 좌우를 탐색하며 1을 찾는다.
        dc = 0
        nc = 0

        # 왼쪽 확인
        if 0 <= c-1 and arr[r][c-1] == 1:
            dc = -1
        elif c+1 < 100 and arr[r][c+1] == 1:
            dc = 1

        if dc:
            nc = c + dc
            while 0 <= nc < 100 and arr[r][nc] == 1:
                nc += dc
            else:
                nc -= dc
                c = nc
        r -= 1
        if r == 0:
            break
    result = c

    print(f"#{tc} {result}")
```



### 1211. Ladder2

- 시작지점의 column 리스트를 저장한다.
- 각 시작지점 별로 탐색을 진행하고, 최소값과 최소값을 갖게 하는 시작 column 위치를 업데이트한다.

```python
# 출발점에서 도착점까지의 거리 구하기

import sys

sys.stdin = open("Ladder2.txt")


N = 100
for _ in range(10):
    tc = int(input())
    ladder = []
    cc_list = []

    for idx in range(N):
        ladder.append(list(map(int, input().split())))
        if idx == 0:
            for c in range(N):
                if ladder[idx][c] == 1:
                    cc_list.append(c)


    min_count = 987654321
    answer = 0
    for idx in range(len(cc_list)):
        cc = cc_list[idx]
        cr = 0
        count = 0
        while cr != 99:
            dc = 0
            if cc > 0 and ladder[cr][cc - 1] == 1:
                dc = -1
            elif cc < 99 and ladder[cr][cc + 1] == 1:
                dc = 1

            if dc:
                while 0 <= cc + dc <= 99 and ladder[cr][cc + dc] == 1:
                    cc += dc
                    count += 1
            cr += 1
            count += 1
        if count < min_count:
            min_count = count
            answer = cc_list[idx]
    print(f"#{tc} {answer}")
```



### 1244_최대 상금

#### 내 코드

##### 메모리 초과

- 불필요한 중복이 너무 많이 생길 것

```python
T = int(input())


def solve(change):
    global answer

    if change == 0:
        temp_number = int("".join(map(str, number_list)))
        answer = max(answer, temp_number)
        return

    for i in range(len(number_list)):
        for j in range(len(number_list)):
            if i == j:
                continue
            # 두 값을 교환
            number_list[i], number_list[j] = number_list[j], number_list[i]
            solve(change - 1)
            # 원래대로
            number_list[i], number_list[j] = number_list[j], number_list[i]

for tc in range(1, T + 1):
    origin_number, change_count = map(int, input().split())
    number_list = list(map(int, str(origin_number)))

    answer = origin_number
    solve(change_count)
    print(f"#{tc} {answer}")
```



- `0`번째 인덱스 부터 `N-1`번째 인덱스까지 순환 [i]
  - `i + 1`부터 `N - 1`까지 수를 비교하며, `i`번째 값보다 큰 값들 중 가장 큰 값을 찾는다. [`idx`]
  - `i`번째 값과 `idx`번째 값을 교환한다.

##### 오답

- 32888에 대한 답을 88823으로 하였다.

```python
# 두 인덱스에 있는 값을 교환을 했을 때, 교환을 하지 않았을 때로 구분하여 생각

T = int(input())


for tc in range(1, T + 1):
    origin_num, change_count = map(int, input().split())
    num_list = [int(x) for x in str(origin_num)]
    N = len(num_list)

    change = 0
    i = 0
    while change < change_count and i < N:
        idx = i
        num = num_list[i]
        # i + 1번째 인덱스 부터 N - 1번째 인덱스까지의 수 중 i번째 인덱스보다 크면서 가장 큰 수를 찾기
        for j in range(i + 1, N):
            if num <= num_list[j]:
                idx = j
                num = num_list[j]
        # 두 값을 교환
        num_list[i], num_list[idx] = num_list[idx], num_list[i]
        change += 1
        i += 1
    # 교환 횟수가 남아있지 않다면?
    if change == change_count:
        answer = int("".join(map(str, num_list)))
    # 교환 횟수가 남아있다면?
    else:
        # 남은 교환 횟수가 짝수라면, 더이상 교환할 필요가 없다.
        if (change_count - change) % 2 == 0:
            answer = int("".join(map(str, num_list)))
        # 남은 교환 횟수가 홀수라면, 가장 영향이 적도록 만들어주어야 한다.
        else:
            # 중복되는 숫자가 있다면, 그 숫자들끼리 교환하면 되기에 전체 값에는 영향을 주지 않는다.
            duplicated = False
            for i in range(N):
                for j in range(N):
                    if i == j:
                        continue
                    if num_list[i] == num_list[j]:
                        duplicated = True
            if duplicated:
                answer = int("".join(map(str, num_list)))
            else:
                # 영향이 적게 만들어주려면 가장 작은 두 값을 교환한다.
                num_list[-1], num_list[-2] = num_list[-2], num_list[-1]
                answer = int("".join(map(str, num_list)))
    print(answer)

```







