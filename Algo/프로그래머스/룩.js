// N 룩

// 문제 설명
// 체스 게임에는 룩(Rook)이라는 말이 있습니다. 아래 그림과 같이 룩은 현재 놓인 위치에서 가로, 혹은 세로방향으로 원하는 만큼 이동이 가능합니다. 만약 룩이 이동 가능한 위치에 다른 말이 있다면 그 말을 잡을 수 있습니다.(장기의 차車와 유사합니다.)

// n x n 크기의 체스판 위에 k개의 룩을 서로 잡을 수 없는 위치에 올려놓으려고 합니다. 예를 들어 n이 3이고, k가 2라면 아래 그림과 같이 배치할 수 있고, 가능한 경우의 수는 총 18개입니다.

// image

// 체스판의 크기 n과 룩(Rook)의 개수 k가 주어졌을때, 체스판 위에 서로 잡을 수 없도록 룩을 배치하는 경우의 수를 반환하는 함수 solution을 완성해주세요. 단, 체스판을 회전해서 같은 경우는 고려하지 않으며, 숫자가 매우 커질 수 있으므로 가능한 경우의 수를 10,007로 나눈 나머지를 반환해야 합니다.

// 제한사항
// 체스판의 크기 n : 1 ≤ n ≤ 31
// 룩(Rook)의 개수 k : 0 ≤ k ≤ 312
// 입출력 예
// n	k	result
// 2	2	2
// 3	2	18
// 입출력 예 설명
// 입출력 예 #1
// 2x2 크기의 체스판에 2개의 룩(Rook)을 서로 잡을 수 없도록 올려놓는 방법은 2가지입니다.

// 입출력 예 #2
// 3x3 크기의 체스판에 2개의 룩(Rook)을 서로 잡을 수 없도록 올려놓는 방법은 모두 18가지입니다.

function solution(n, k) {
  let answer = 0
  let visitedColumns = Array(n).fill(false)

  if (k === 0) {
    return 0
  }

  function rook(cr, count) {
    if (count === k) {
      answer += 1
      return
    }

    if (cr >= n || n - cr + 1 < k - count) {
      return
    }

    for (let c = 0; c < n; c++) {
      if (visitedColumns[c]) {
        continue
      }
      visitedColumns[c] = true
      rook(cr + 1, count + 1)
      visitedColumns[c] = false
      rook(cr + 1, count)
    }
  }

  rook(0, 0)
  return answer % 10007
}

console.log(solution(2, 1))
