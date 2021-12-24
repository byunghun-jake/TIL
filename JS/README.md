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



## 17장 생성자 함수에 의한 객체 생성

### 17-1. Object 생성자 함수 ❌

new 연산자와 함께 Object 생성자 함수를 호출하여 객체를 생성할 수 있다.

```javascript
const person = new Object()

person.name = "김병훈"
person.sayHello = function() {
    console.log(`안녕! ${this.name}`)
}
console.log(person)	// {name: "김병훈", sayHello: f}
person.sayHello		// 안녕! 김병훈
```

#### 생성자 함수

생성자 함수: new 연산자와 함께 호출하여 객체(인스턴스)를 생성하는 함수

### 17-2. 생성자 함수

#### 객체 리터럴 방식의 문제점

> 유사한 여러 객체를 생성할 때, 반복 작업을 해야한다.

```javascript
const circle1 = {
    radius: 5,
    // 반복
    getDiameter() {
        return 2 * this.radius
    }
}
const circle2 = {
    radius: 10,
    // 반복
    getDiameter() {
        return 2 * this.radius
    }
}
```



#### 생성자 함수의 장점

> 프로퍼티 구조가 동일한 객체 여러 개를 간편하게 생성할 수 있다.

```javascript
function Circle(radius) {
    this.radius = radius
    this.getDiameter = function() {
        return 2 * this.radius
    }
}

const circle1 = new Circle(5)
const circle2 = new Circle(10)
```

##### new

new 연산자와 함께 호출해야 생성자 함수로서 동작한다.

new 연산자를 함께 사용하지 않으면 일반 함수로 동작한다.

```javascript
const circle3 = Circle(3)
console.log(circle3)	// undefined
// Circle 함수는 반환값이 없다.

console.log(radius)	// 3
// Circle 함수가 실행되며, this는 전역 객체를 가리키게 되고
// 전역 객체에 radius와 getDiameter가 등록된다.
```



##### this

this는 객체 자신의 프로퍼티나 메서드를 참조하기 위한 자기 참조 변수이다. this가 가리키는 값, this 바인딩은 함수 호출 방식에 따라 **동적으로 결정**된다.

| 함수 호출 방식       | this가 가리키는 값                      |
| -------------------- | --------------------------------------- |
| 일반 함수로서 호출   | 전역 객체 (window / global)             |
| 메서드로서 호출      | 메서드를 호출한 객체 (마침표 앞의 객체) |
| 생성자 함수로서 호출 | 생성자 함수가 생성할 인스턴스           |

```javascript
function foo() {
    console.log(this)
}
const obj = {
    foo
}

foo()	// window
obj.foo()	// obj
const inst = new foo()	// inst
```



#### 생성자 함수의 인스턴스 생성 과정

> 생성자 함수에서 해야하는 것은?
>
> 1. 인스턴스 생성
> 2. 생성된 인스턴스 초기화 (인스턴스의 프로퍼티를 추가하고 그 값을 초기화하는 것)

##### 1. 인스턴스 생성과 this 바인딩

암묵적으로 빈 객체가 생성된다. (인스턴스)

인스턴스(빈 객체)가 this에 바인딩된다.

```javascript
function Circle(radius) {
    // 1. 암묵적으로 인스턴스가 생성되고, this에 바인딩된다.
    console.log(this)	// Circle {}
    
    // ...
}
```

##### 2. 인스턴스 초기화

생성자 함수에 적힌 코드가 한 줄씩 실행되며, this에 바인딩되어 있는 인스턴스에 프로퍼티와 메서드를 추가하고, 전달받은 초기값을 할당한다.

```javascript
function Circle(radius) {
    // 1. 암묵적으로 인스턴스가 생성되고, this에 바인딩된다.
    console.log(this)	// Circle {}
    
    // 2. 인스턴스 초기화
    this.radius = radius
    this.getDiameter = function() {
        return 2 * this.radius
    }
}
```

##### 3. 인스턴스 반환

생성자 함수 내의 처리가 끝 => 완성된 인스턴스가 바인딩된 this가 암묵적으로 반환된다. (변수에 할당)

```javascript
function Circle(radius) {
    // 1. 암묵적으로 인스턴스가 생성되고, this에 바인딩된다.
    console.log(this)	// Circle {}
    
    // 2. 인스턴스 초기화
    this.radius = radius
    this.getDiameter = function() {
        return 2 * this.radius
    }
}

// 3. 인스턴스 생성(반환)
const circle1 = new Circle(10)
console.log(circle1)	// Circle {radius: 10, getDiameter: f}
```

만약 생성자 함수에서 다른 객체를 명시적으로 (return문을 통해) 반환한다면, 암묵적으로 반환할 예정이었던 this는 무시한다.

```javascript
function Circle(radius) {
    // 1. 암묵적으로 인스턴스가 생성되고, this에 바인딩된다.
    console.log(this)	// Circle {}
    
    // 2. 인스턴스 초기화
    this.radius = radius
    this.getDiameter = function() {
        return 2 * this.radius
    }
    
    return {}
}
const circle2 = new Circle(100)
console.log(circle2)	// {}
```

생성자 함수에서 객체가 아닌 원시값을 반환한다면, 원시값을 무시하고 this를 반환한다.

```javascript
function Circle(radius) {
    // 1. 암묵적으로 인스턴스가 생성되고, this에 바인딩된다.
    console.log(this)	// Circle {}
    
    // 2. 인스턴스 초기화
    this.radius = radius
    this.getDiameter = function() {
        return 2 * this.radius
    }
    
    return 10000000000000000000000000000000000000000000000000
}
const circle3 = new Circle(100)
console.log(circle3)	// Circle {radius: 100, getDiameter: f}
```

#### 함수 (callable / constructor & non-constructor)

함수는 객체이다. 하지만 일반 객체와는 다르다.

> 일반 객체는 호출할 수 없지만, 함수는 호출할 수 있다.

모든 함수는 호출할 수 있지만(callable), 모든 함수를 생성자 함수로 호출할 수 있는 것은 아니다.

---

자바스크립트 엔진은 함수가 어떻게 정의되어있는지를 평가하여 함수가 생성자 함수로 호출할 수 있는지 아닌지를 구분한다.

- constructor: 함수 선언문, 함수 표현식, 클래스
- non-constructor: 메서드, 화살표 함수

```javascript
// 함수 선언문
function constructor1() {}
// 함수 표현식
const constructor2 = function() {}
const x = {
    constructor3: function() {}
}

new constructor1()
new constructor2()
new x.constructor3()
```

```javascript
// 화살표 함수
const nonCon1 = () => {}
// 메서드(ES6 축약형)
const x = {
    nonCon2() {}
}
new nonCon1()	// TypeError: nonCon1 is not a constructor
new x.nonCon2()	// TypeError: x.nonCon2 is not a constructor
```



#### new 연산자

new 연산자 없이 함수를 호출하면 내부 메서드 `[[Call]]`이 호출된다.

new 연산자와 함께 함수를 호출하기 위해서는 해당 함수가 constructor이어야 하며, 내부 메서드 `[[Construct]]`가 호출된다.

##### new.target

생성자 함수가 new 연산자 없이 호출되는 것을 방지하기 위해 ES6에서 도입되었다.

함수 내부에서 `new.target`을 사용하면, new 연산자와 함께 호출되었는지 아닌지 확인할 수 있다.

> new 연산자와 함께 생성자 함수로서 호출되었다면: `new.target === 함수 자신`
>
> 일반 함수로서 호출되었다면: `new.target === undefined`

```javascript
function Circle(radius) {
    if (!new.target) {
        // new 연산자와 함께 호출되지 않았다면
        // 생성자 함수를 재귀 호출하여 생성된 인스턴스를 반환한다.
        return new Circle(radius)
    }
    // ...
}
```

##### 스코프 세이프 생성자 패턴

```javascript
function Circle(radius) {
    if (!(this instanceof Circle)) {
        return new Circle(radius)
    }
    // ...
}
```



## 18장 함수와 일급 객체

### 18-1. 일급 객체

객체 중에 일급 객체가 되려면, 어떤 조건을 가지고 있어야 할까?

1. 무명의 리터럴로 생성할 수 있다. 즉, 런타임에 생성이 가능하다.
2. 변수나 자료구조(배열, 객체 등)에 저장할 수 있다.
3. 함수의 매개변수에 전달할 수 있다.
4. 함수의 반환값으로 사용할 수 있다.

```javascript
// 1. 익명 함수로 생성
// 2. 함수는 변수에 저장할 수 있다.
// 런다임에 함수 리터럴이 평가되어 함수 객체가 생성되고, 변수에 할당된다.
const increase = function(num) {
    return ++num
}
const decrease = function(num) {
    return --num
}

// 2. 함수는 객체나 배열에 저장할 수 있다.
const arr = [increase, decrease]
const predicates = {
    increase,
    decrease,
}

// 3. 함수의 매개변수에 전달할 수 있다.
// 4. 함수의 반환값으로 사용할 수 있다.
function makeCounter(predicate) {
    let num = 0
    return function() {
        num = predicate(num)
        return num
    }
}

const increaser = makeCounter(predicates.increase)
console.log(increaser())

const decreaser = makeCounter(predicates.decrease)
console.log(decreaser())
```

### 18-2. 함수 객체의 프로퍼티

함수는 객체이기에 프로퍼티를 가질 수 있다.

```javascript
function square(num) {
    return num * num
}
console.dir(square)
// ƒ square(number)
// arguments: null
// caller: null
// length: 1
// name: "square"
// prototype: {constructor: ƒ}
// [[FunctionLocation]]: VM5172:1
// [[Prototype]]: ƒ ()
// [[Scopes]]: Scopes[1]

console.log(Object.getOwnPropertyDescriptors(square))
// {length: {…}, name: {…}, arguments: {…}, caller: {…}, prototype: {…}}
// arguments: {value: null, writable: false, enumerable: false, configurable: false}
// caller: {value: null, writable: false, enumerable: false, configurable: false}
// length: {value: 1, writable: false, enumerable: false, configurable: true}
// name: {value: 'square', writable: false, enumerable: false, configurable: true}
// prototype: {value: {…}, writable: true, enumerable: false, configurable: false}
// [[Prototype]]: Object
```

#### 1. arguments

arguments 객체는 Key (인수의 순서) - Value (인수의 값)로 구성되어 있다. 배열 형태로 인자 정보를 담고 있지만, 실제 배열이 아닌 유사 배열 객체이다.

> 유사 배열 객체: length 프로퍼티를 가진 객체로 for문으로 순회할 수 있는 객체를 말한다.

arguments 객체는 매개변수 개수를 확정할 수 없는 **가변 인자 함수**를 구현할 때 유용하다.

```javascript
function sum() {
    let res = 0
    for (let i = 0; i < arguments.length; i++) {
        res += arguments[i]
    }
    return res
}

console.log(sum())			// 0
console.log(sum(1, 2))		// 3
console.log(sum(1, 2, 3))	// 6
```

```javascript
function sum() {
    const array = Array.prototype.slice.call(arguments)
    return array.reduce(function (pre, cur) {
        return pre + cur
    }, 0)
}
```

ES6에서는 Rest 파라미터가 도입되었다.

```javascript
function sum(...args) {
    return args.reduce((pre, cur) => pre + cur, 0)
}
```

#### 2. caller 프로퍼티

#### 3. length 프로퍼티

함수를 정의할 때 선언한 매개변수의 개수

> arguments 프로퍼티 객체의 length는 인자(argument)의 개수를 가리키고,
>
> 함수의 length 프로퍼티는 매개변수(parameter)의 개수를 가리킨다.

```javascript
function foo() {}
console.log(foo.length)	// 0
function bar(x) {
    return x
}
console.log(bar.length)	// 1
```

#### 4. name 프로퍼티

함수 이름을 나타낸다.

```javascript
// 함수 표현식
const namedFunc = function foo() {}
const anonymousFunc = function() {}
console.log(namedFunc.name)		// foo
console.log(anonymousFunc.name)	// ES5: ""	// ES6: anonymousFunc

// 함수 선언문
function bar() {}
console.log(bar.name)			// bar
```



## 19장 프로토타입

자바스크립트는 프로토타입 기반 객체지향 프로그래밍을 지원하는 프로그래밍 언어이다.

원시 타입(Number, String, Boolean, Symbol, Null, Undefined)을 제외한 모든 것은 객체이다.

### 19-1. 객체지향 프로그래밍

프로그램을 명령어 또는 함수의 목록으로 보는 전통적인 명령형 프로그래밍의 절차지향적 관점에서 벗어나

여러 개의 독립적 단위, 즉 객체의 집합으로 프로그램을 표현하려는 프로그래밍 패러다임을 말한다.

다양한 속성 중에서 프로그램에 필요한 속성만 간추려 내어 표현하는 것을 추상화라 한다.

```javascript
const person = {
    name: "Lee",
    address: "Seoul",
    hello() {
        console.log("안녕하세요")
    }
}
```

> 이처럼 객체지향 프로그래밍은 객체의 상태를 나타내는 데이터와 상태 데이터를 조작할 수 있는 동작을 하나의 논리적인 단위로 묶어 생각한다.
>
> 객체: 상태 데이터와 동작을 하나의 논리적 단위로 묶은 복합적인 자료구조



## 25장 클래스

자바스크립트에서 클래스는 기존 프로토타입 기반 패턴을 클래스 기반 패턴"처럼" 사용할 수 있도록 하는 문법적 설탕 (Syntactic sugar)이라고 볼 수 있다.

클래스와 생성자 함수의 차이

- 클래스를 new 연산자 없이 호출하면 에러가 발생한다.

  > 생성자 함수는 new 없이 호출하면 일반 함수로서 호출된다.

- 클래스는 상속을 지원하는 `extends`, `super` 키워드를 제공한다.

- 클래스는 호이스팅이 발생하지 "않는 것 처럼" 동작한다.

  > 함수 선언문 `function FunctionName() {}` 으로 정의된 생성자 함수는 함수 호이스팅이, 함수 표현식 `var FunctionVal = function () {}`으로 정의한 생성자 함수는 변수 호이스팅이 발생한다.

- 클래스 내 모든 코드에는 암묵적으로 `strict mode`가 지정되어있다.

- 클래스의 constructor, 프로토타입 메서드, 정적 메서드는 모두 프로퍼티 어트리뷰트 `[[Enumerable]]`의 값이 false다. 열거 불가

이러한 차이들로 클래스를 프로토타입 기반 객체 생성 패턴의 단순한 문법적 설탕이라고 보기보다는 새로운 `객체 생성 메커니즘`으로 보는 것이 더 합당하다.

### 클래스 정의

```js
// 클래스 선언문
class Person {}

// 익명 클래스 표현식
const Person = class {}

// 기명 클래스 표현식
const Person = class ClassName {}
```

클래스는 함수다. 자바스크립트에서 함수는 일급 객체이다.

=> 클래스는 일급 객체이다.



일급 객체로서 클래스의 특징

- 무명의 리터럴로 생성 가능 === 런타임에 생성 가능
- 변수나 자료구조(객체, 배열 등)에 할당 가능
- 함수의 매개변수에 전달 가능
- 함수의 반환값으로 사용 가능



### 클래스 호이스팅

클래스는 함수다. 함수 선언문으로 정의한 함수는 호이스팅이 이루어진다.

클래스 선언문으로 정의한 클래스도 마찬가지로 소스코드 평가 과정(런타임 이전)에 평가되어 객체를 생성한다. 이때 클래스가 평가되어 생성된 함수 객체는 constructor다.

클래스는 클래스 정의 이전에 참조할 수 없다. (호이스팅이 일어나는 것과는 별개)

```js
console.log(Person)
// ReferenceError: Cannot access "Person" before initialization

class Person {}
```

> 호이스팅이 일어나지 않는 것 처럼 보일 수 있다.



```js
const Person = "내가 출력되면, 호이스팅이 일어나지 않는 것이겠지"

{
    console.log(Person)
    // ReferenceError: Cannot access "Person" before initialization
    
    class Person {}
}
```

> `{}` 내의 코드에 대한 평가가 이루어 질 때, `class Person {}`에 대한 호이스팅(등록)이 이루어지지 않았다면 외부의 `Person`을 출력해야 한다.
> 하지만, 결과는 참조 에러.
> 참조를 못하는 것일 뿐 호이스팅이 일어난다는 것을 확인할 수 있다.



### 인스턴스 생성

클래스는 생성자 함수이다.

new 연산자와 함께 호출되어 인스턴스를 생성한다.



```js
class Person = {}

const me = new Person()
const you = Person()	// TypeError: Class constructor Person cannot be invoked without "new"
```



### 메서드

클래스 몸체에는 0개 이상의 메서드"만" 정의할 수 있다.

메서드 종류: constructor, 프로토타입 메서드, 정적 메서드

```js
class Person {
    // constructor (생성자)
    // 프로퍼티 생성 및 초기화
    constructor(name) {
        this.name = name
    }
    
    // 프로토타입 메서드
    sayHi() {
        console.log(`안녕, 내 이름은 ${this.name}이야.`)
    }
    
    static sayHello() {
        console.log(`Hi!`)
    }
}

const me = new Person("김병훈")

console.log(me.name)	// 김병훈
me.sayHi()				// 안녕, 내 이름은 김병훈이야.
Person.sayHello()		// Hi!
```



#### 생성자 메서드 constructor

constructor는 인스턴스를 생성하고, 초기화하기 위한 특수 메서드이다.

constructor 내부에서 this에 추가한 프로퍼티는 해당 클래스가 생성한 인스턴스의 프로퍼티가 된다.

```js
class Person {
    constructor(name) {
        this.name = name
    }
}

const me = new Person("김병훈")
console.log(me)	// {name: "김병훈"}

// 생성자 함수 내부에서 this에 추가하는 방식과 대응된다.
function Person (name) {
    this.name = name
}
```



class의 constructor와 생성자 함수의 차이점

- constructor는 클래스 내에 최대 한 개만 존재할 수 있다.
  생략이 가능하지만, 암묵적으로 빈 constructor `constructor() {}`가 정의된다.
- 인스턴스 프로퍼티의 초기값을 전달할 때, 그것을 받는 부분은 constructor이다.



주의할 점

> constructor 함수 내에 반환문은 갖지 않아야 한다.
> constructor는 암묵적으로 this를 반환하는데, 반환문이 명시되어 있으면 this가 아닌 반환문에 해당하는 내용을 반환하게 된다.
> 이는 클래스의 동작을 깨는 방식이기에 해서는 안된다.



#### 프로토타입 메서드

```js
// 생성자 함수 내에서 프로토타입 메서드를 정의하는 방법
function Person(name) {
    this.name = name
    
    Person.prototype.sayHi = function() {
        console.log(`Hi! ${this.name}`)
    }
}

// 클래스에서 프로토타입 메서드를 정의하는 방법
class Person {
    constructor(name) {
        this.name = name
    }
    
    sayHi() {
        console.log(`Hi! ${this.name}`)
    }
}
```

> sayHi는 Person 클래스의 메서드라고 생각할 수 있지만,
> 실제로는 Person의 prototype에 있는 메서드이다.



#### 정적 메서드

인스턴스를 생성하지 않아도 호출할 수 있는 메서드

```js
// 생성자 함수에 정적 메서드를 추가하기
function Person(name) {...}

Person.sayHi = function() {}

// 정적 메서드 호출
Person.sayHi()
```

```js
// 클래스에 정적 메서드 추가하기
class Person {
    constructor() {
        // ...
    }
    
    static sayHi() {
        // ...
    }
}

Person.sayHi()
```



정적 메서드는 인스턴스로 호출할 수 없다.

인스턴스의 프로토타입 체인에 클래스가 존재하지 않기 때문

(인스턴스) => (클래스의 프로토타입)

```js
const me = new Person("김병훈")
me.sayHi()	// TypeError: me.sayHi is not a function
```



#### 프로토타입 메서드와 정적 메서드의 차이

- 프로토타입 메서드는 클래스의 프로토타입에 바인딩 되어 있다.
  정적 메서드는 클래스에 바인딩 되어 있다.
- 프로토타입 메서드는 인스턴스에서 호출이 가능하다.
  정적 메서드는 인스턴스에서 호출이 불가능하다.
- 프로토타입 메서드는 인스턴스의 프로퍼티를 참조할 수 있다.
  정적 메서드는 인스턴스의 프로퍼티를 참조할 수 없다.

> 이 차이들은 결국, 메서드가 어느 객체에 바인딩 되어 있느냐에 따른 것



### 인스턴스 생성 과정

1. 인스턴스 생성과 this 바인딩

   new 연산자와 함께 클래스를 호출 => 암묵적으로 빈 객체(인스턴스) 생성 => 클래스의 프로토타입 객체를 인스턴스의 프로토타입으로 설정 => 인스턴스는 this에 바인딩

2. 인스턴스 초기화

   constructor 내부 코드 실행 (this에 바인딩 되어 있는 인스턴스 초기화)

   인스턴스에 프로퍼티 추가 => constructor 인수가 받은 값으로 프로퍼티 값을 초기화

3. 인스턴스 반환

   constructor 코드 종료 => 인스턴스에 바인딩된 this가 반환된다.



### 상속에 의한 클래스 확장

```js
class Animal {
    constructor(age, weight) {
        this.age = age
        this.weight = weight
    }
    eat() {return "eat"}
    move() {return "move"}
}

class Bird extends Animal {
    fly() {return "fly"}
}

class Lion extends Animal {
    attack() {return "attack"}
}
```

> 코드 재사용성을 높이고, 중복된 코드 작성을 방지할 수 있다.



#### super 키워드

##### super 호출

super를 호출하면 수퍼클래스의 constructor를 호출한다.

- 서브클래스에서는 constructor를 생략하지 않는 한, 반드시 super를 호출해야 한다. (Error 발생)
- 서브클래스의 constructor에서 super를 호출하기 전에는 this를 참조할 수 없다.
- super는 반드시 서브클래스의 constructor에서 호출해야 한다. 프로토타입 메서드나 정적 메서드에서 호출하면 에러 발생

##### super 참조

메서드 내에서 super를 참조하면, 수퍼클래스의 메서드를 호출할 수 있다.

- 서브클래스의 프로토타입 메서드 내에서 super.sayHi는 수퍼클래스의 프로토타입 메서드 sayHi를 가리킨다.

  ```js
  class Base {
      sayHi() {
          console.log("Base의 프로토타입 메서드")
      }
  }
  
  class SubClass extends Base {
      sayHi() {
          super.sayHi()
      }
  }
  
  const sub = new SubClass()
  sub.sayHi()	// Base의 프로토타입 메서드
  ```

  

#### 상속 클래스의 인스턴스 생성 과정

```js
class Rectangle {
    constructor (width, height) {
        this.width = width
        this.height = height
    }
    
    getArea() {
        return this.width * this.height
    }
    
    toString() {
        return `width: ${this.width}, height: ${this.height}`
    }
}

class ColorRectangle extends Rectangle {
    constructor(width, height, color) {
        super(width, height)
        this.color = color
    }
    
    // 프로토타입 메서드 오버라이딩 (덮어쓰기)
    toString() {
        return super.toString() + `, color: ${this.color}`
    }
}

const r1 = new ColorRectangle(2, 4, "red")
console.log(r1.gerArea())	// 8
console.log(r1.toString())	// width: 2, height: 4, color: red
```

1. 서브클래스의 super 호출

   서브클래스는 직접 인스턴스를 생성하지 않고, 수퍼클래스에게 인스턴스 생성을 위임한다.

   > 서브클래스의 constructor에서 반드시 super를 호출해야 하는 이유

   super를 호출하면, 수퍼클래스의 constructor를 호출하는 것이다. 수퍼클래스가 평가되어 생성된 함수 객체의 코드가 실행된다.

2. 수퍼클래스 인스턴스 생성과 this 바인딩

   수퍼클래스 코드가 실행되면서, 인스턴스가 생성된다.

   new 연산자와 호출된 클래스는 서브클래스이기에 인스턴스는 서브클래스가 생성하는 것으로 처리된다.

3. 수퍼클래스 인스턴스 초기화

   수퍼클래스의 constructor가 실행되면서, this에 바인딩 되어 있는 인스턴스를 초기화한다.

4. 서브클래스 constructor 복귀와 this 바인딩

   서브클래스에서 호출한 super가 종료되고, 제어 흐름이 서브클래스 constructor로 복귀한다.

   수퍼클래스가 반환한 인스턴스가 서브클래스의 this에 바인딩된다.

   서브클래스는 인스턴스를 직접 생성하지 않고, 수퍼클래스가 반환한 인스턴스를 이어받아 작업을 진행한다.

   > 서브클래스의 constructor에서 this 초기화 코드 이전에 super를 호출해야 하는 이유!

5. 서브클래스 인스턴스 초기화

   서브클래스에 전달된 인자로 인스턴스의 프로퍼티를 초기화한다.

6. 인스턴스 반환

   서브클래스의 constructor가 종료되며, 인스턴스가 바인딩된 this가 반환된다.



## 26장 ES6 함수의 추가 기능

### 함수의 구분

ES6 이전의 함수는 new 연산자와 함께 호출하면 생성자 함수이고, 그렇지 않으면 일반 함수가 된다.
=> constructor 이자, callable 이다.

이는 객체 내부의 함수, 메서드에도 동일하게 적용되는데, 이는 성능 면에서 문제가 된다. (함수의 인자로 전달하는 콜백함수도 마찬가지)
=> 객체에 바인딩 된 함수가 constructor라는 것은 객체에 바인딩된 함수가 prototype 프로퍼티를 가지며, 프로토타입 객체도 생성한다는 것을 의미하기 때문

뭐든 다 할 수 있는 함수를 그대로 사용하는 것 보다는 용도에 맞도록 제한되는 방식으로 구분하자!

| ES6 함수 구분 | constructor | prototype | super | arguments |
| ------------- | ----------- | --------- | ----- | --------- |
| 일반 함수     | O           | O         | X     | O         |
| 메서드        | X           | X         | O     | O         |
| 화살표 함수   | X           | X         | X     | X         |

### 메서드

ES6 사양에서 메서드란, 메서드 축약 표현으로 정의된 함수만을 의미한다.

```js
const obj = {
    name: "김병훈",
    callMe() {
        console.log("나는 non-constructor이다.")
    },
    callMe2: function() {
        console.log("나는 constructor이다.")
    }
}

new obj.callMe()	// TypeError: obj.callMe is not a contrutctor
```



### 화살표 함수

```js
const sum = (a, b) => {
    return a + b
}

// 즉시 실행 함수
const person = (name => ({
    sayHi() { return `Hi! My name is ${name}` }
}))("Kim")
```



#### 화살표 함수와 일반 함수의 차이

1. 인스턴스를 생성할 수 없는 `non-constructor`이다.

   - new 연산자로 호출할 수 없다.
   - prototype 프로퍼티가 없다.

2. 중복된 매개변수 이름을 선언할 수 없다.

   ```js
   function sum (a, a) { return a + a }
   console.log(sum(1, 2))	// 4
   
   const sum = (a, a) => a + a	// SyntaxError: Duplicate parameter name not allowed in this context
   ```

   > 일반 함수도 strict mode에서는 SyntaxError가 발생한다.

3. 함수 자체의 this, arguments, super, new.target 바인딩을 갖지 않는다.

   화살표 함수 내에서 this, arguments, super, new.target을 참조하면, 스코프 체인을 통해 상위 스코프의 this, arguments, super, new.target을 참조한다.



#### this

화살표 함수가 일반 함수와 가장 큰 차이를 보이는 부분

this 바인딩은 함수의 호출 방식, 즉 함수가 어떻게 호출 되었느냐에 따라 동적으로 결정된다. (렉시컬 스코프)

이때, 주의할 것은 콜백 함수인 경우.
고차함수의 인수로 전달되어 고차 함수 내부에서 호출되는 콜백 함수도 중첩 함수라 할 수 있다.

```js
class Perfixer {
    constructor(prefix) {
        this.prefix = prefix
    }
    
    add(arr) {
        return arr.map(function(item) {
            return this.prefix + item
            // TypeError: Cannot read property 'prefix' of undefined
        })
    }
}

const prefixer = new Prefixer("-webkit-")
console.log(prefixer.add(["transition", "user-select"]))
```

> add 메서드에서 this는 메서드를 호출한 객체를 가리킨다. `prefixer.add(...)` 방식으로 호출하기 때문
>
> Array.prototype.map으로 전달한 콜백 함수인 `funtion(item) {}` 은 일반 함수로 호출한다. 따라서 내부의 this는 undefined를 가리킨다.
> 원래는 일반 함수 내부의 this는 전역 객체를 가리키지만, 클래스 내부의 모든 코드는 strict mode가 적용되기 때문에 undefined가 바인딩되는 것이다.



위 문제를 해결하기 위해 ES6 이전에 했던 작업

```js
// ...
add(arr) {
    var that = this
    return arr.map(function(item) {
        return that.prefix + item
    })
}

// map은 두번째 인자로 콜백함수의 this와 바인딩 할 객체를 전달할 수 있다.
add(arr) {
    return arr.map(function(item) {
        return this.prefix + item
    }, this)
}

// bind 메서드를 이용해 바인딩
add(arr) {
    return arr.map(function(item) {
        return this.prefix + item
    }.bind(this))
}
```



ES6 화살표 함수 도입 후

```js
class Perfixer {
    constructor(prefix) {
        this.prefix = prefix
    }
    
    add(arr) {
        return arr.map((item) => this.prefix + item)
    }
}

const prefixer = new Prefixer("-webkit-")
console.log(prefixer.add(["transition", "user-select"]))
```

> 화살표 함수는 함수 자체의 this 바인딩을 갖지 않는다.
> 화살표 함수 내부에서 this를 참조하면, 상위 스코프로 이동하여 this를 찾아 참조한다.
>
> 이를 렉시컬 this라고 한다.



### Rest 파라미터

Rest 파라미터는 함수에 전달된 인수의 목록을 배열로 전달받는다.

```js
function foo(...rest) {
    console.log(rest)	// [1, 2, 3, 4]
}

foo(1, 2, 3, 4)
```

> 가변 인자 함수의 인수 목록을 배열로 전달받을 수 있어 편리하다.



## 27장 배열

### 배열

배열은 여러 개의 값을 순차적으로 나열한 자료구조이다.

배열 생성

> 배열 리터럴, Array 생성자 함수, Array.of, Array.from 메서드로 생성할 수 있다.



배열의 배열 요소
