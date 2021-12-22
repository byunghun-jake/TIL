// 최대 N잔, 동시에 추출 가능한 커피 추출기
// 만들어야 하는 커피 M잔: 커피에 주문번호 1 ~ M
// 주문번호 순으로 빈 커피 추출구에서 커피 제작
// if 빈 추출구가 없다면 => 다음 주문 대기
// if 빈 추출구가 생기면 => 다음 커피 만들기 시작

// 커피 별로 제조 시간이 다르다.

// N: 커피를 한 번에 추출할 수 있는 개수
// coffee_times: 각 커피 만드는 데 걸리는 시간 []
// 커피가 완성되는 순서대로 주문번호를 배열에 담아 리턴
// if 커피 추출이 동시에 완료 => 작은 주문번호가 앞에 오도록 한다.

class Coffee {
  constructor(time, idx) {
    this.time = time
    this.idx = idx
    this.next = null
    this.prev = null
  }
}

class CoffeeMachine {
  constructor(maxSize) {
    this.head = null
    this.tail = null
    this.maxSize = maxSize
    this.size = 0
    this.minTime = 200000000
  }
  append(time, idx) {
    const newCoffee = new Coffee(time, idx)
    if (this.head === null) {
      this.head = newCoffee
      this.tail = newCoffee
    } else {
      this.tail.next = newCoffee
      newCoffee.prev = this.tail
      this.tail = newCoffee
    }
    if (time < this.minTime) {
      this.minTime = time
    }
    this.size += 1
  }

  updateMinTime() {
    this.minTime = 200000000
    let coffee = this.head
    while (coffee) {
      if (coffee.time < this.minTime) {
        this.minTime = coffee.time
      }
      coffee = coffee.next
    }
  }

  check(queue) {
    const finishCoffeeList = []
    let coffee = this.head
    while (coffee) {
      coffee.time -= this.minTime
      if (coffee.time === 0) {
        finishCoffeeList.push(coffee.idx)
        this.size -= 1
        if (coffee === this.head) {
          this.head = coffee.next
        } else if (coffee === this.tail) {
          this.tail = coffee.prev
          coffee.prev.next = coffee.next
        } else {
          coffee.prev.next = coffee.next
          coffee.next.prev = coffee.prev
        }
      }
      coffee = coffee.next
    }

    while (this.size < this.maxSize && queue.size) {
      const [time, idx] = queue.dequeue()
      this.append(time, idx)
    }

    coffee = this.head
    while (coffee) {
      console.log(coffee)
      coffee = coffee.next
    }

    this.updateMinTime()
    return finishCoffeeList.sort((a, b) => a - b)
  }
}

class Queue {
  constructor() {
    this.head = null
    this.tail = null
    this.size = 0
  }
  enqueue(time, idx) {
    const newCoffee = new Coffee(time, idx)
    if (this.head === null) {
      this.head = newCoffee
      this.tail = newCoffee
    } else {
      this.tail.next = newCoffee
      this.tail = newCoffee
    }
    this.size += 1
  }
  dequeue() {
    if (this.size === 0) {
      return null
    }
    const time = this.head.time
    const idx = this.head.idx
    this.head = this.head.next
    this.size -= 1
    return [time, idx]
  }
}

function solution(N, coffee_times) {
  var answer = []
  const timeQueue = new Queue()
  coffee_times.forEach((time, idx) => {
    timeQueue.enqueue(time, idx + 1)
  })
  const coffeeMachine = new CoffeeMachine(N)
  for (let i = 0; i < N; i++) {
    const coffee = timeQueue.dequeue()
    if (coffee === null) {
      break
    }
    coffeeMachine.append(coffee[0], coffee[1])
  }
  while (coffeeMachine.size) {
    const result = coffeeMachine.check(timeQueue)
    if (result.length) {
      answer.push(...result)
    }
  }
  return answer
}

console.log(solution(3, [4, 2, 2, 5, 3]))
