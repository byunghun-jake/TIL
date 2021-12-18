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

function solution(priorities, location) {
  const queue = new Queue()
  const prioritiesQueue = new Queue()
  priorities.forEach((priority, i) => {
    queue.enqueue([priority, i === location])
  })
  priorities
    .sort((a, b) => b - a)
    .forEach((priority) => {
      prioritiesQueue.enqueue(priority)
    })

  let count = 1
  while (queue.size) {
    const [priority, isMine] = queue.dequeue()
    if (priority === prioritiesQueue.head.value) {
      prioritiesQueue.dequeue()
      if (isMine) {
        return count
      }
      count += 1
    } else {
      queue.enqueue([priority, isMine])
    }
  }
}

console.log(solution([2, 1, 3, 2], 2))
