# Regex



## DreamCoding



### Groups ans ranges

`|` 또는

`()` 그룹

`/gr(e|a)y/gm`: gray, grey

`(?:)` 찾지만, 그룹으로 기억하지는 않는다.

`[]` 문자셋, 괄호안의 어떤 문자든

`/gr[a-z]y/gm`: gray ~ grzy

`[^]` 부정 문자셋, 괄호안의 문자가 아닐때



### Quantifiers

`?` 없거나, 하나 있거나(zero or one)

`*` 없거나, 있거나 (zero or more)

`+` 있다 (one or more)

`{n}` n번 반복하여 있다

`{min, }` min번 이상 있다.

`{min, max}` min번 이상, max번 이하 있다.



### Boundary-type

#### 단어 기준

`\b`: 단어 경계

`/Ap\b/gm`: Ap 중에서 문자의 끝에 있는 경우만

`/\b/Ap/gm`: Ap 중에서 문자의 시작에 있는 경우만



`\B`: 단어 경계가 아님

`/Ap\B/gm`: Ap 중에서 문자의 끝에 있지 않은 경우만



#### 문장 기준

> multi-line Flag가 있어야 한다.

`^`: 문장의 시작

`/^abc/gm`: `abc`들 중에서 문장의 시작 위치에 있는 경우만



`$`: 문장의 끝

`/xyz$/gm`: `xyz` 중에서 문장의 끝 위치에 있는 경우만



### Character classes

`\`: 특수 문자가 아닌 문자

`/./gm`는 임의의 글자를 찾는다. 문자 중에서 온점(.)을 찾고 싶다면?

`/\./gm`: 온점(.)을 찾는 정규표현식



`.`: 임의의 글자



> 소문자가 True, 대문자는 False

`/\d/gm`: digit 숫자

`/\D/gm`: digit 숫자가 아닌 문자

`/\w/gm`: word 문자

`/\W/gm`: word 문자가 아닌 문자

`/\s/gm`: space 공백

`/\S/gm`: space 공백이 아닌 문자



### Flag

- g: global
- i: case insensitive
- m: multiline
- s: single line (dotall)
- u: unicode
- y: sticky

보편적으로 g와 m을 사용한다.



### Test

#### 1. 전화번호 체크

```
010-898-0893
010 898 0893
010.898.0893
010-405-3412
02-878-8888
```

```
/\d{2,3}[-. ]\d{3}[-. ]\d{4}/gm
```

