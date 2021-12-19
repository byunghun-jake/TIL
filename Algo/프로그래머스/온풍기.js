function solution(office, k) {
  let answer = -1
  const N = office.length
  for (let r = 0; r < N - k + 1; r++) {
    for (let c = 0; c < N - k + 1; c++) {
      let count = 0
      for (let cr = r; cr < r + k; cr++) {
        for (let cc = c; cc < c + k; cc++) {
          if (office[cr][cc] === 1) {
            count += 1
          }
        }
      }
      if (count > answer) {
        answer = count
      }
    }
  }
  return answer
}

console.log(
  solution(
    [
      [1, 0, 0, 0],
      [0, 0, 0, 1],
      [0, 0, 1, 0],
      [0, 1, 1, 0],
    ],
    2
  )
)
