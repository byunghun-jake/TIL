## 1. 자료구조

메모리를 효율적으로 사용하여 빠르고 안정적으로 데이터를 처리하기 위해, 상황에 따라 유용하게 사용될 수 있도록 특정 구조를 이루고 있다.

> 상황에 따라 유용 => 잘못 사용하는 경우에는 비효율적일 수 있다.

> 완벽한 자료구조는 없다.
>
> 더 좋고, 더 나쁜 자료구조는 없으며, 특정 상황에서 유용한 자료구조와 덜 유용한 자료구조로 나누어 질 뿐이다.

자료구조는 크게 3개의 구조로 나뉜다.

1. 단순 구조
   1. 정수
   2. 실수
   3. 문자열
   4. 논리
2. 선형 구조
   1. 배열
   2. 연결 리스트
   3. 스택
   4. 큐
3. 비선형 구조
   1. 트리
   2. 그래프



### 선형 구조

1차원 형태의 데이터 구조

한 원소 뒤에 하나의 원소만이 존재하는 형태. 자료들이 선형으로 나열되어 있는 구조를 가진다.

선형 구조에 해당되는 자료구조는 **배열, 연결 리스트, 스택, 큐** 등이 있다.

### 비선형 구조

원소 간 M:N 관계를 가지는 구조. 계층으로 구분되는 구조나 망 형태로 되어있는 구조를 표현하기에 적합하다.

비선형 구조에 해당되는 자료구조는 트리, 그래프 등이 있다.



## 2. 시간복잡도

프로그램의 성능을 제대로 알 수 있을까?

프로그램의 성능을 확인하기 위해 고려할 것들은 다양하다.
입력 크기, 하드웨어 성능, 운영체제 성능, 컴파일러 최적화, 비동기 로직 등

=> 프로그램의 성능을 정확히 파악하는 것은 불가능하다.
상대적인 성능 확인



### 빅 오 표기법

![image-20211216212809822](README.assets/image-20211216212809822.png)



### 프로그램 성능 확인

#### Date 객체 이용

```javascript
const start = new Date().getTime()

// ...
const end = new Date().getTime()

console.log(end - start)
```



## 자바스크립트 코드 트릭

### 1. 구조 분해 할당 (destructuring assignment)

```javascript
let age1 = 30
let age2 = 40
[age1, age2] = [age2, age1]
console.log(age1, age2)	// 40 30
```



### 2. 배열 생성으로 루프 순회하기

```javascript
const sum = Array
	.from(new Array(4), (_, k) => k + 5)
	.reduce((arr, cur) => arr + cur, 0)
```

#### Array.from

유사 배열 객체를 배열로 바꾸는 데 사용

첫 번째 인자로는 유사 배열 객체, 두 번째 인자로는 배열 각 셀에 값을 넣을 수 있도록 콜백함수를 받는다.

> 두 번째 인자로 받는 콜백 함수에 전달되는 첫 번째 인자는 유사 배열 객체의 값이고, 두 번째 인자는 셀의 인덱스이다.

```javascript
Array.from("tei")	// ["t", "e", "i"]

Array.from([1, 2, 3], x => x * x)	// [1, 4, 9]

Array.from({length: 4})	// [undefined, undefined, undefined, undefined]

Array.from({length: 2}, () => Array(2).fill(0))	// [[0, 0], [0, 0]]
```



### 3. 배열 내 같은 요소 제거하기 (중복 제거)

```javascript
const names = ["김", "이", "박", "최", "노", "김", "김"]
const uniqueNamesWithArrayFrom = Array.from(new Set(names))	// ["김", "이", "박", "최", "노"]
const uniqueNamesWithSpread = [...new Set(names)]			// ["김", "이", "박", "최", "노"]
```

#### Set

중복을 허용하지 않는 값을 모아놓은 컬렉션

- `new Set(iterable)`



### 4. 객체 병합하기

```javascript
const obj1 = {
    name: "kim",
    age: 30,
    city: "gunpo",
}

const obj2 = {
    age: 31,
    city: "sokcho",
}

console.log({...obj1, ...obj2})	// {name: "kim", age: 31, city: "sokcho"}
console.log({...obj2, ...obj1})	// {name: "kim", age: 30, city: "gunpo"}
```



### 5. ||와 && 활용

```javascript
// ||
// 기본값을 할당할 때 사용
const name = nullableValue || "Unknown"

// &&
// 조건부 실행 혹은 할당
booleanValue && func()

const getCompany = (showAddress) => ({
    name: "혼냅",
    ...showAddress && {address: "Seoul"},
})
console.log(getCompany(false))	// {name: "혼냅"}
console.log(getCompany(true))	// {name: "혼냅", address: "Seoul"}
```



### 6. 구조 분해 할당 사용 

```javascript
const person = {
    name: "kim",
    age: 30,
    city: "sokcho",
}

const {age, city} = person
```



### 7. 비구조화 할당 사용, 객체 생성시 키 생략

```javascript
const makeCompany = ({name, address, serviceName}) => ({
    name,
    address,
    serviceName,
})

const matchere = makeCompany({ name: "매치히어", address: "온라인", serviceName: "매치히어" })
```



### 8. 동적 속성 이름

```javascript
const TAB_TYPE = {
    KEYWORD: "KEYWORD",
    HISTORY: "HISTORY",
}

const TAB_LABEL = {
    [TAB_TYPE.KEYWORD]: "추천 검색어",
    [TAB_TYPE.HISTORY]: "최근 검색어",
}
```



### 9. !! 연산자를 이용하여 Boolean 값으로 변경하기

```javascript
function check (variable) {
    if (!!variable) {
        console.lor(variable, "truthy")
    } else {
        console.log(variable, "falsy")
    }
}

check(0)			// 0, "falsy"
check(null)			// null, "falsy"
check(undefined)	// undefined, "falsy"
check(false)		// false, "falsy"
check("")			// <empty string>, "falsy"
check(NaN)			// NaN, "falsy"
```



## 3. 배열

### 배열의 특징

- 고정된 크기를 가지며, 일반적으로는 동적으로 크기를 늘릴 수 없다.

  > 자바스크립트는 동적으로 크기가 증감되도록 만들어져 있다.

- 원하는 원소의 index를 알고 있다면 `O(1)`의 시간 복잡도로 원소를 찾을 수 있다.
- 원소를 삭제하면 해당 index에 빈자리가 생긴다.

#### 자바스크립트에서 배열의 특징

- 자바스크립트의 배열은 동적으로 크기가 증감되도록 만들어져 있다.

- 자바스크립트의 배열은 HashMap에 가깝다.

  > index가 number 타입이 아니어도 된다.



#### 배열 요소 삭제

배열의 요소를 삭제하는 경우 최대 `O(n)` 시간 복잡도가 소요된다.

#### 배열 요소 추가

배열의 요소를 추가하는 경우 최대 `O(n)` 시간 복잡도가 소요된다.



**=> 추가와 삭제가 반복되는 로직이라면, 배열 자료구조는 권장하지 않는다.**

---

### JS에서 사용법

#### 배열 생성

```javascript
// 1.
// 빈 array를 생성 (리터럴)
let arr1 = []

// 2.
// 초기화된 array를 생성
let arr2 = [1, 2, 4, 8]

// 3.
// Array 생성자 활용
let arr3 = Array(4).fill(0)
// [0, 0, 0, 0]

// 4.
// 유사 배열 객체와 Array.from 메서드를 활용
let arr4 = Array.from({length: 100}, (_, i) => i)
// [0, 1, 2, ...]
```



#### 배열 요소 추가, 삭제

> splice 메서드는 최대 O(n) [선형 시간]이 소요된다.

```js
let arr = [1, 2, 3]

arr.push(4)	// O(1)
arr.push(5, 6)	// O(1)
arr.splice(3, 0, 128)	// O(n)
// [1, 2, 3, 128, 4, 5, 6]

arr.pop()	// O(1)
arr.splice(3, 1)	// O(n)
// [1, 2, 3, 4, 5, 6]
```





































