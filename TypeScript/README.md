### Type Assertions

TypeScript는 알지 못하지만, 개발자 입장에서 명확히 타입을 아는 경우 타입을 강제로 지정해주는 데 사용한다.



`document.getElementById`를 통해 Element를 가져온다면, TypeScript는 리턴 값이 `HTMLElement` 종류겠거니~ 생각 할 것이다.

하지만, 가져오는 Element가 항상 `HTMLCanvasElement`임을 알고 있다면 가져오는 Element의 타입을 지정해줄 수 있을 것이다.

```typescript
// 1. as-syntax
const myCanvas = document.getElementById("main_canvas") as HTMLCanvasElement

// 2. 'angle-bracket' syntax
const myCanvas = <HTMLCanvasElement>document.getElementById("main_canvas")
```

> Reminder: Because type assertions are removed at compile-time, there is no runtime checking associated with a type assertion. There won’t be an exception or `null` generated if the type assertion is wrong.