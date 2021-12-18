class Node {
  constructor(value) {
    this.value = value
    this.next = null
  }
}

class Queue {
  constructor() {
    this.head = null
    this.tail = null
    this.size = 0
  }

  enqueue(value) {
    const newNode = new Node(value)
    if (this.head === null) {
      this.head = this.tail = newNode
    } else {
      this.tail.next = newNode
      this.tail = newNode
    }
    this.size += 1
  }

  dequeue() {
    const value = this.head.value
    this.head = this.head.next
    this.size -= 1
    return value
  }
}

function solution(progresses, speeds) {
  const answer = []
  const queue = new Queue()
  progresses.forEach((progress, i) => {
    queue.enqueue([progress, speeds[i]])
  })

  while (queue.size) {
    let cNode = queue.head
    while (cNode) {
      const [p, s] = cNode.value
      cNode.value = [p + s, s]
      cNode = cNode.next
    }
    cNode = queue.head
    let count = 0
    while (cNode && cNode.value[0] >= 100) {
      queue.dequeue()
      count += 1
      cNode = queue.head
    }
    if (count > 0) {
      answer.push(count)
    }
  }
  console.log(answer)
  return answer
}

solution([93, 30, 55], [1, 30, 5])
