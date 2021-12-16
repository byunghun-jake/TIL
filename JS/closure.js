// 1. counter

let num1 = 0

const increase1 = function () {
  return ++num1
}

console.log(increase1())
console.log(increase1())
console.log(increase1())

// num1은 전역변수로, increase1에 의해서만 관리되고 있지 않다.
// 외부 요인에 의해 값이 변경될 수 있다.

// 2. 함수 내부에 상태값 넣기

const increase2 = function () {
  let num2 = 0

  return ++num2
}

console.log(increase2()) // 1
console.log(increase2()) // 1
console.log(increase2()) // 1

// 함수가 실행될 때마다 num2가 다시 선언되고 0으로 초기화된다.
// 상태가 유지되지 않는다.

// 3. 클로저 활용

const increase3 = (function () {
  let num3 = 0

  return function () {
    return ++num3
  }
})()

console.log(increase3())
console.log(increase3())
console.log(increase3())

// 즉시 실행함수로 increase3에는 익명함수의 중첩익명함수(클로저)가 할당된다.
// 중첩익명함수는 익명함수의 num3를 참조하고 있기 때문에 num3는 메모리에서 삭제되지 않는다.

// 4. 클로저 활용 2

const counter = (function () {
  let num = 0

  return {
    increase() {
      return ++num
    },
    decrease() {
      return --num
    },
  }
})()

console.log(counter.increase())
console.log(counter.increase())
console.log(counter.increase())
console.log(counter.increase())
console.log(counter.decrease())
console.log(counter.decrease())
console.log(counter.decrease())
console.log(counter.decrease())

// 클로저 활용 전 (캡슐화, 정보은닉)

function Person1(name, age) {
  this.name = name
  const _age = age

  this.sayHi = function () {
    console.log(`내 이름은 ${this.name}이고, 나이는 ${_age}야`)
  }
}

const me1 = new Person1("김병훈", 30)
console.log(me1.name)
console.log(me1._age)
me1.sayHi()
me1.name = "이름을 변경할 수 있어"
me1.sayHi()

// name은 public, _age는 private
// sayHi 메서드는 공통인데 인스턴스를 만들때마다 생성된다. (최적화 x)

// sayHi를 Prototype을 통해 생성
function Person2(name, age) {
  this.name = name
  const _age = age
}

Person2.prototype.sayHi = function () {
  console.log(`내 이름은 ${this.name}이고, 나이는 ${_age}야`)
}

const me2 = new Person2("김병훈", 30)
// me2.sayHi()
// _age를 참조할 수 없다. 함수 외부에서 참조하고 있기 때문

const Person3 = (function () {
  let _age = 0

  function Person3(name, age) {
    this.name = name
    _age = age
  }

  Person3.prototype.sayHi = function () {
    console.log(`내 이름은 ${this.name}이고, 나이는 ${_age}야`)
  }

  return Person3
})()

const me3 = new Person3("김병훈", 3000)
const you3 = new Person3("너", 20)
me3.sayHi()
you3.sayHi()

// Prototype 메서드를 이용할 때 문제 발생!

// 자주 하는 실수
const funcs = []

for (let i = 0; i < 3; i++) {
  funcs[i] = function () {
    return i
  }
}

for (let i = 0; i < funcs.length; i++) {
  console.log(funcs[i]())
}
