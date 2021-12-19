// 구간합

function solution(estimates, k) {
  let answer = 0
  let total = 0
  for (let i = 0; i < k; i++) {
    total += estimates[i]
  }
  answer = total
  for (let i = 1; i < estimates.length - k + 1; i++) {
    total = total - estimates[i - 1] + estimates[i + k - 1]
    if (answer < total) {
      answer = total
    }
  }
  return answer
}

// function solution(estimates, k) {
//   let answer = 0
//   for (let i = 0; i < estimates.length - k + 1; i++) {
//     let total = 0
//     for (let j = i; j < i + k; j++) {
//       total += estimates[j]
//     }
//     if (answer < total) {
//       answer = total
//     }
//   }
//   return answer
// }

console.log(solution([5, 1, 9, 8, 10, 5], 3))
