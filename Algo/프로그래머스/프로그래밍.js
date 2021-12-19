// 뒤에서부터 순회
// 높이와 인덱스를 저장할 스택 생성
// 타겟 지점의 높이와 스택의 top과 비교
// 타겟 지점의 높이 >= 스택 top의 높이 => 스택 pop
// 타겟 지점의 높이 < 스택 top의 높이 => 기간 입력 (스택 top의 인덱스 - 타겟 지점의 인덱스), 스택 push(타겟 지점 높이, 인덱스)

function solution(price) {
  let answer = []
  let stack = []
  for (let i = price.length - 1; i > -1; i--) {
    const targetPrice = price[i]
    if (i === price.length - 1) {
      answer.push(-1)
      stack.push([targetPrice, i])
    } else {
      for (let j = stack.length - 1; j > -1; j--) {
        const [topPrice, topIndex] = stack[j]
        if (targetPrice < topPrice) {
          answer.push(topIndex - i)
          stack.push([targetPrice, i])
          break
        } else {
          stack.pop()
        }
      }
      if (stack.length === 0) {
        answer.push(-1)
        stack.push([targetPrice, i])
      }
    }
  }
  return answer.reverse()
}

// function solution(price) {
//   let answer = []
//   price.forEach((p, index) => {
//     answer[index] = -1
//     for (let i = index + 1; i < price.length; i++) {
//       if (p < price[i]) {
//         answer[index] = i - index
//         break
//       }
//     }
//   })
//   return answer
// }

console.log(solution([13, 7, 3, 7, 5, 16, 12]))
