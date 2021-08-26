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

