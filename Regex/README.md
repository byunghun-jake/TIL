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

`\b`: 단어 경계

`/Ap\b/gm`: Ap 중에서 문자의 끝에 있는 경우만

`/\b/Ap/gm`: Ap 중에서 문자의 시작에 있는 경우만



`\B`: 단어 경계가 아님

`/Ap\B/gm`: Ap 중에서 문자의 끝에 있지 않은 경우만



### Flag

- g: global
- i: case insensitive
- m: multiline
- s: single line (dotall)
- u: unicode
- y: sticky

보편적으로 g와 m을 사용한다.

