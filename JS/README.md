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



# DreamCoding

## Event

### Event bubbling & Event capturing

부모 요소에서 자식 요소로 (실제 이벤트가 발생한 위치까지) 찾아가는 것: 이벤트 캡처링

자식 요소에서 발생한 이벤트가 부모 요소로 전달되어 확산되는 것: 이벤트 버블링

### Event delegation (이벤트 위임)

> 공통 부모 안에 여러 자식 요소에 이벤트를 등록해야 하는 경우, 직접 자식에게 이벤트를 등록하지 않고 부모 요소에 이벤트를 등록해 target을 이용하여 이벤트를 핸들링하는 방법

```html
<html>
    <body>
        <ul>
            <li>1</li>
            <li>2</li>
            <li>3</li>
            <li>4</li>
        </ul>
    </body>
    <script>
    	// bad
        const lis = document.querySelectorAll("li")
        lis.forEach(li => {
            li.addEventListener("click", () => {
                li.classList.toggle("selected")
            })
        })
        // Good
        const ul = document.querySelector("ul")
        ul.addEventListener("click", (event) => {
          console.log(event.target.tagName)
          const target = event.target.closest("li")
          if (target) {
            target.classList.toggle("selected")
          }
        })
    </script>
</html>
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



## 13장 - 스코프



### 13.1 스코프란?

모든 식별자(변수 이름, 함수 이름, 클래스 이름 등)는 "**자신이 선언된 위치에 따라 다른 코드가 그 식별자를 참조할 수 있는 범위(유효 범위)가 결정된다.**"

- 스코프: 식별자의 유효 범위

```js
var x = "global"

function foo() {
    var x = "local"
    console.log(x)	// local
}

console.log(x)	// global
```

자바스크립트 엔진은 두 개 이상의 변수 중에서 어떤 변수를 참조해야 하는지 결정해야 하는데, 이를 "**식별자 결정(identifier resolution)**"이라 한다.
식별자 결정 시 스코프를 이용하는데, 이는 곧 "스코프란 자바스크립트 엔진이 식별자를 결정할 때 사용하는 규칙"이라고 할 수 있는 것이다.



### 13.2 스코프의 종류

| 구분 | 설명                  | 스코프      | 변수      |
| ---- | --------------------- | ----------- | --------- |
| 전역 | 코드의 가장 바깥 영역 | 전역 스코프 | 전역 변수 |
| 지역 | 함수 몸체 내부        | 지역 스코프 | 지역 변수 |

- 전역 변수는 어디서든 참조할 수 있다.
- 지역 변수의 스코프는 자신이 속한 지역 스코프 + 하위 지역 스코프이다.
- 상위 스코프에서 유효한 변수는 하위 스코프에서도 참조할 수 있지만, 하위 스코프에서 유효한 변수를 상위 스코프에서 참조할 수 없다.



### 13.5 렉시컬 스코프

- 렉시컬 스코프: 

- 자바스크립트는 렉시컬 스코프를 따르므로, 함수를 어디서 정의했는지에 따라 상위 스코프를 결정한다.
- 함수가 호출된 위치는 영향을 주지 않는다.



## 14장 전역 변수의 문제점

### 14.1 변수의 생명 주기

- 변수는 선언에 의해 생성되고, 할당에 의해 값을 갖는다. 그리고 소멸한다. (Life Cycle)

- 변수에 생명 주기가 없다면, 한번 선언된 변수는 없어지지 않고 메모리 공간을 차지할 것이다.

- 함수 내부에서 선언된 지역변수는 함수가 호출되면 생성되고, 함수가 종료되면 소멸한다.

  => 지역 변수의 생명 주기 == 함수의 생명 주기



- 호이스팅은 스코프를 단위로 동작한다.

  전역 변수의 선언이 전역 스코프의 선두로 끌어올려진 것처럼, 지역 변수의 호이스팅은 지역 변수의 선언이 지역 스코프 선두로 끌어올려진 것 처럼 동작한다.

- 호이스팅은 변수 선언이 스코프의 선두로 끌어올려진 것처럼 동작하는 자바스크립트 고유의 특징을 말한다.

### 14.2 전역 변수의 문제점

#### 암묵적 결합

전역 변수는 전역에서 참조가 가능하고, 변경할 수 있는 암묵적 결합을 허용한다.

#### 긴 생명주기

전역 변수는 코드가 종료될 때 까지 살아 있다.

== 전역 변수는 생명 주기가 길다

#### 스코프 체인 상에서 가장 마지막에 존재

- 변수를 검색할 때 전역 변수가 가장 마지막에 검색된다.

  == 전역 변수의 검색속도가 가장 느리다.

#### 네임스페이스 오염

다른 파일에 동일한 이름으로 선언된 경우 예상하지 못한 결과를 가져올 수 있다.

### 14.3 전역 변수의 사용을 억제하는 방법

> 전역 변수를 사용해야 할 이유를 찾지 못했다면, 지역 변수를 사용해야 한다.
>
> 변수의 스코프는 좁을수록 좋다.

1. 즉시 실행 함수

   즉시 실행 함수는 함수 정의와 동시에 호출된다.

   함수 내부에 정의된 변수들은 함수 호출과 함께 소멸된다. 곧, 모든 변수가 즉시 실행 함수의 지역 변수가 되는 것.

2. 네임스페이스 객체 💩

   전역에 네임스페이스를 담당할 객체를 생성하고, 전역 변수로 사용할 변수를 프로퍼티로 추가하는 방식

   ```js
   var MYAPP = {}
   
   MYAPP.name = "김병훈"
   
   console.log(MYAPP.name)	// 김병훈
   ```

3. 모듈 패턴😎

   모듈 패턴은 자바스크립트의 강력한 기능인 "클로저"를 기반으로 동작한다.

   모듈 패턴은 전역 변수의 억제와 함께 캡슐화를 구현할 수 있다.

   ```js
   var Counter = (function() {
       // private 변수
       var num = 0
       
       return {
           increase() { return ++num },
           decrease() { return --num }
       }
   }())
   
   console.log(Counter.num)	// undefined
   console.log(Counter.increase())	// 1
   console.log(Counter.decrease())	// 0
   ```

4. ES6 모듈

   ES6 모듈은 파일 자체의 독자적인 모듈 스코프를 제공한다.

   ```html
   <script type="module" src="lib.mjs"></script>
   <script type="module" src="app.mjs"></script>
   ```

   

## 15장 let, const 키워드와 블록 레벨 스코프

### 1. var 키워드로 선언한 변수의 문제점

1. 변수 중복 선언 허용

   ```javascript
   var x = 1
   
   var x = 100
   
   console.log(x) // 100
   ```

   > 이미 선언된 변수를 재선언하며, 문제가 발생할 수 있다.

2. 함수 레벨 스코프

   ```javascript
   var x = 1
   if (true) {
       var x = 100
   }
   console.log(x) // 100
   ```

   > 함수 레벨 스코프는 전역 변수를 남발하는 상황을 유발할 수 있다.

3. 변수 호이스팅

   변수 호이스팅에 의해 선언 이전에 해당 변수를 참조할 수 있다.

   ```javascript
   console.log(x) // undefined
   var x = 100
   console.log(x) // 100
   ```

   > 프로그램의 흐름 상 맞지 않기에 가독성을 떨어뜨린다.

### 2. let 키워드

#### 2-1. 변수 중복 선언 금지

```javascript
let x = 10
console.log(x)	// 10
x = 100
console.log(x)	// 100

let x = 1000	// SyntaxError: Identifier "x" has already been declared
console.log(x)
```



#### 2-2. 블록 레벨 스코프

```javascript
let x = 10
if (true) {
    console.log(x)	// 10
    let x = 100
    let y = 200
    console.log(x)	// 100
}
console.log(x)		// 10
console.log(y)		// ReferenceError: y is not defined
```

let 키워드로 선언한 변수는 모든 코드 블록(`if`, `for`, `while`, `try/catch` 등)을 스코프로 인정하는 **블록 레벨 스코프**를 따른다.



#### 2-3. 변수 호이스팅

```javascript
console.log(x)	// ReferenceError: x is not defined
let x = 100
```

var 키워드로 선언한 변수는 런타임 이전에 자바스크립트 엔진에 의해 암묵적으로 "선언 단계"와 "초기화 단계"가 진행된다.
선언 단계에서 실행 컨텍스트의 환경에 변수 식별자를 등록하여 자바스크립트 엔진에 변수가 존재한다는 사실을 인지할 수 있게 된다.
초기화 단계에서 해당 변수를 `undefined`로 초기화한다.

let 키워드로 선언한 변수는 "선언 단계"와 "초기화 단계"가 분리되어 진행된다.
런타임 이전에 자바스크립트 엔진에 의해 "선언 단계"가 실행되지만, "초기화 단계"는 변수 선언문에 도달하였을 때 실행된다.

> **!중요!**
>
> **let 키워드로 선언한 변수가 호이스팅이 발생하지 않는 것이 아니다.**
> 변수 선언에 도달하기 전까지 "초기화"가 이루어지지 않을 뿐, "선언"은 런타임 이전에 이루어 진다.

```javascript
let x = 1
if (true) {
    console.log(x)	// ReferenceError: Cannot access "x" before initialization
    let x = 100
}
```

호이스팅이 이루어지지 않았다면, `console.log(x)`는 1을 출력했었어야 했다.
하지만, 초기화되지 않은 x를 참조하지 못한다는 에러가 발생했다. 이는, `if`문 안의 `let x = 100`에 의해 내부 x는 이미 선언된 상태라는 것이고, 초기화 되기 전에 변수를 참조하려고 하였기 때문에 일시적 사각 지대(Temporal Dead Zone) 상태인 x에 의해 에러가 발생하는 것이다.

---

> 호이스팅
>
> 런타임 전, 자바스크립트 엔진에 의해 선언문에 의해 선언된 변수 또는 함수(클래스)가 실행 컨텍스트의 스코프에 등록되는 것
>
> 자바스크립트는 ES6에서 도입된 let, const를 포함하여 모든 선언(var, let, const, function, class 등)을 호이스팅한다. 단, let, const, class를 사용한 선언문은 호이스팅이 발생하지 않는 것처럼 동작한다.

---

### 3. const 키워드

#### 3-1. 선언과 초기화

const 키워드로 선언한 변수는 선언과 동시에 초기화해야 한다. 

```javascript
const foo	// SyntaxError: Mission initializer in const declaration
```

#### 3-2. 재할당 금지

const 키워드로 선언한 변수는 재할당 할 수 없다.

```javascript
const foo = 1
foo = 10	// TypeError: Assignment to constant variable.
```

#### 3-3. 상수

const 키워드의 특성 상, const는 상수를 표현하는 데 사용하기도 한다.

```javascript
const TAX_RATE = 0.1
let preTaxPrice = 100

let afterTaxPrice = preTaxPrice + (preTaxPrice * TAX_RATE)
```

#### 3-4. 객체

const 키워드를 이용하여 원시값을 선언한 경우에는 변경할 수 없다. 이는 값에 의한 참조를 하고 있기 때문에, 원시값을 변경할 수 없어 일어나는 특성이다.

하지만, const 키워드를 이용하여 객체를 선언한 경우에는 객체 내부의 프로퍼티는 변경할 수 있다.

```javascript
const person = {
    name: "김병훈"
}
person.name = "비타민"
console.log(person.name)	// 비타민
```



## 16장 프로퍼티 어트리뷰트

자바스크립트 엔진은 프로퍼티를 생성할 때, 프로퍼티의 상태를 나타내는 **프로퍼티 어트리뷰트**를 기본값으로 자동 정의한다.

프로퍼티의 상태:

1. 프로퍼티의 값(value)
2. 값의 갱신 가능 여부(writable)
3. 열거 가능 여부(enumerable)
4. 재정의 가능 여부(configurable)

```javascript
const person = {
    name: "김병훈"
}
console.log(Object.getOwnPropertyDescriptor(person, "name"))
// {value: '김병훈', writable: true, enumerable: true, configurable: true}
```

```javascript
const person = {
    name: "김병훈"
}
person.age = 30
console.log(Object.getOwnPropertyDescriptors(person))
// age: {value: 30, writable: true, enumerable: true, configurable: true}
// name: {value: '김병훈', writable: true, enumerable: true, configurable: true}
```



### 데이터 프로퍼티 & 접근자 프로퍼티

#### 데이터 프로퍼티

키와 값으로 구성된 일반적인 프로퍼티.

#### 접근자 프로퍼티

자체적으로는 값을 갖지 않고 다른 데이터 프로퍼티의 값을 읽거나 저장할 때 호출되는 접근자 함수로 구성된 프로퍼티

> ex) getter / setter

```javascript
const person = {
    firstName: "병훈",
    lastName: "김",
    get fullName() {
        return `${lastName} ${firstName}`
    },
    set fullName(name) {
        [this.lastName, this.firstname] = name.split(" ")
    }
}

console.log(Object.getOwnPropertyDescriptors(person))
//	firstName: {value: '병훈', writable: true, enumerable: true, configurable: true}
//	lastName: {value: '김', writable: true, enumerable: true, configurable: true}
//	fullName: {enumerable: true, configurable: true, get: ƒ, set: ƒ}
```

> 데이터 프로퍼티: firstName / lastName
>
> 접근자 프로퍼티: fullName



