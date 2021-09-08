### Javascript sort array of objects by a boolean property

```js
a = [false, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, false, true, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false];
    
    
a.sort(function(x, y) {
    // true values first
    return (x === y)? 0 : x? -1 : 1;
    // false values first
    // return (x === y)? 0 : x? 1 : -1;
});

console.log(a);
```



# DeepDive



## 12장 함수

### 12.1 함수란?

- argument(인수), parameter(매개 변수), return value(반환 값)
- 함수 선언(function definition)으로 함수를 정의
- 함수 호출(function invoke/call)을 통해 함수를 실행



### 12.2 함수를 사용하는 이유

- 코드의 재사용

  필요할 때 여러 번 호출할 수 있다.

- 유지보수의 편의성을 높이고, 코드의 신뢰성을 높일 수 있다.

  코드를 재사용함으로써 생기는 이점

- 코드의 가독성

  함수의 이름은 함수의 역할을 잘 설명할 수 있어야 한다.



### 12.3 함수 리터럴

> 리터럴: 사람이 이해할 수 있는 문자 또는 약속한 기호를 사용해 "값"을 생성하는 표기법(notation)

함수 리터럴도 평가되어 값을 생성하며, 함수 리터럴은 객체를 생성하는 표기법이다.

함수 == 객체

#### 함수 리터럴의 구성 요소

1. 함수 이름
2. 매개변수 목록
3. 함수 몸체



### 12.4 함수 정의

#### 함수 정의 방식

1. 함수 선언문

   ```js
   function add(x, y) {
       return x + y
   }
   ```

2. 함수 표현식

   ```js
   const add = function (x, y) {
       return x + y
   }
   ```

3. function 생성자 함수

   ```js
   const add = new Function('x', 'y', 'return x + y')
   ```

4. 화살표 함수

   ```js
   const add = (x, y) => {
       return x + y
   }
   ```

#### 선언과 정의

변수는 선언 variable declaration

함수는 정의 function definition

함수 선언문이 평가되면, 식별자가 암묵적으로 생성되고 함수 객체가 할당된다.

#### 12.4.1 함수 선언문

함수 리터럴과 형태가 동일하다.

함수 리터럴은 "함수 이름"을 생략할 수 있으나, 함수 선언문은 생략할 수 없다.

함수 선언문은 표현식(값을 반환하는)이 아니라 문(값을 반환하지 않는)이다.

```js
console.log(function(a, b) {return a + b})
// undefined
```

`표현식이 아닌 문`은 값을 반환하지 않기 때문에 변수에 할당할 수 없다. 하지만 함수 표현식 예제를 보면 변수에 할당하는 것을 볼 수 있다.

```js
// Function Expression
const add = function add(x, y) {
    return x + y
}

console.log(add(1, 4)) // 5
```

자바스크립트 엔진이 문맥에 따라 두 가지로 해석하기 때문

1. 함수 선언문: 표현식이 아닌 문
2. 함수 리터럴 표현식: 표현식인 문



함수는 함수 이름으로 호출하는 것이 아니라, 함수 객체(가 저장된 메모리)를 가리키는 식별자로 호출한다.

```js
const add: 식별자 = function add: 함수 이름(x, y) {
    return x + y
}

console.log(add: 식별자(1, 4))
```



#### 12.4.2 함수 표현식

함수는 객체 타입의 값이다.

함수는 변수에 할당할 수 있고, 배열의 요소로 들어갈 수 있고, 객체의 프로퍼티 값이 될 수도 있다.

=> 이런 값의 성질을 갖는 객체를 **일급 객체**라고 한다.

> 자바스크립트의 함수는 일급 객체이다.

```js
// 함수 표현식
// Function expression
const add = function(x, y) { return x + y }
```

함수 이름은 생략할 수 있으며, 이름이 생략된 함수 === 익명 함수



함수를 호출할 때에는 식별자를 사용해야 하며, 함수 이름을 통해 호출할 때에는 에러가 발생한다.

```js
const add = function a(x, y) { return x + y }

console.log(add(1, 2)) // 3

// 함수 이름은 함수 몸체 내부에서만 유효하다.
console.log(a(1, 2)) // ReferenceError: a is not defined
```



#### 12.4.3 함수 생성 시점과 호이스팅

```js
// 함수 참조
console.dir(add)	// f add(x, y)
console.dir(sub)	// undefined

// 함수 호출
console.log(add(1, 2))	// 3
console.log(sub(1, 2))	// TypeError: sub is not a function

// 함수 선언
function add(x, y) { return x + y }
const sub = function(x, y) { return x - y }
```

|           | 함수 선언문                                          | 함수 표현식                                                  |
| --------- | ---------------------------------------------------- | ------------------------------------------------------------ |
| 생성 시점 | 런타임 이전, 자바스크립트 엔진에 의해 먼저 실행된다. | 런타임에 평가되어 할당문이 실행되는 시점에 함수 객체가 된다. |
| 호이스팅  | 함수 호이스팅 발생                                   | 변수 호이스팅 발생 (할당문(`=`)은 동작 X)                    |
|           |                                                      |                                                              |

함수 호이스팅은 함수를 호출하기 전에 함수를 선언해야 한다는 순서를 무시한다. 따라서, 함수 선언문 대신, 함수 표현식을 사용할 것을 권장한다.



#### 12.4.5 화살표 함수

ES6에 도입되었다.

화살표 함수는 항상 익명 함수로 정의한다.

```js
const add = (x, y) => x + y
// 다른 문 없이 바로 리턴을 하는 경우에는 {}를 생략할 수 있다.

console.log(add(1, 2)) // 3
```



### 12.5 함수 호출

#### 12.5.1 매개 변수(parameter)와 인자(argument)

함수를 실행하기 위해 입력값을 전달해주어야 할 때, 매개 변수를 통해 인자를 전달한다.

```js
const add = (x, y) => x + y
// x, y는 매개 변수

console.log(add(1, 2))
// 1, 2는 인자
```

매개 변수는 함수 몸체 내부에서만 참조할 수 있다. == 매개 변수의 스코프는 함수 내부다.

```js
const add = (x, y) => x + y

console.log(add(2))	// NaN
// 2 + undefined
// 매개 변수는 undefinded로 초기화된 후, 인자가 할당된다.

console.log(add(1, 2, 3)) // 3
// 1 + 2
// 초과된 인수는 무시된다.
// 버려지는 것은 아님, 모든 argument는 암묵적으로 arguments 객체의 프로퍼티로 보관된다.

const sub = function(x, y) {
    console.log(arguments)
    // Arguments(3) [2, 5, 10, callee: f, Symbol(Symbol.iterator: f)]
    return x - y
}
sub(2, 5, 10)
```



#### 12.5.2 인수 확인

1. 자바스크립트 함수는 매개 변수와 인수의 개수가 일치하는지 확인하지 않는다.
2. 자바스크립트는 동적 타입 언어이다. 따라서 매개변수의 타입을 지정할 수 없다.

```js
// 타입 확인
const add = function (x, y) {
    if (typeof x !== "number" || typeof y !== "number") {
        throw new TypeError("인수는 모두 숫자 타입이어야 합니다.")
    }
    return x + y
}

// 매개 변수와 인수의 개수 불일치
// 1. 기본값 설정
const add = function (x = 0, y = 0) {
    return x + y
}

console.log(add(2)) // 2
```



### 12.6 참조에 의한 전달과 외부 상태의 변경

원시 값은 값을 전달하며, 객체는 참조 값을 전달한다.

객체를 함수의 인자로 전달한다면, 함수의 매개 변수는 동일한 객체를 참조하게 되고 객체를 변경하면 함수 외부에 있던 객체에 영향이 간다.

```js
const changeVal = function(primitive, obj) {
    primitive += 100
    obj.name = "김병훈"
}

const num = 100
const person = {
    name: "이름",
}

changeVal(num, person)

// 원시 값은 원본이 회손되지 않는다.
console.log(num)	// 100
// 객체는 원본 값이 회손된다.
console.log(person)	// { name: "김병훈" }
```

- 함수가 외부 상태를 변경하면, 상태 변화를 추적하기 어려워진다.

- 코드의 복잡성을 증가시키고, 가독성을 해친다.



### 12.7 다양한 함수 형태

#### 12.7.1 즉시 실행 함수(IIFE)

함수 정의와 동시에 즉시 호출되는 함수

단 한 번만 호출되며, 다시 호출할 수 없다.

반드시 그룹 연산자 `(...)`로 감싸야 한다.

```js
// 익명 함수(일반적)
(
	function() {
        const a = 1
        const b = 10
        return a + b
    }
)

// 기명 함수
(
	function add() {
        const a = 1
        const b = 10
        return a + b
    }
)

add()	// ReferenceError: add is not defined
```

그룹 연산자 내부의 문에 의해 함수 객체가 생성되고, 그룹 연산자에 의해 바로 실행이 된다.

#### 12.7.4 콜백함수

함수의 매개 변수를 통해 다른 함수의 내부로 전달되는 함수 => 콜백 함수

매개 변수를 통해 함수의 외부에서 콜백 함수를 전달받은 함수 => 고차 함수

함수형 프로그래밍 뿐만 아니라, 비동기 처리(이벤트 처리, Ajax 통신)



#### 12.7.5 순수 함수와 비순수 함수

순수 함수: 어떤 외부 상태에 의존하지 않고 변경하지 않는, 부수 효과가 없는 함수

비순수 함수: <-->





























