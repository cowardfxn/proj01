# async/await

`util.callbackify(function)`  Takes a function that returns a Promise or an async function, returns a callback style function

async function return a Promise by default. 
async/await can also be used on Promise functions


#### use async/await in serial

```
async function f1() {
    let valueA = await functionA(),
        valueB = await functionB(valueA),
        valueC = await functionC(valueA, valueB);

    return valueC;
}
```

#### use async/await execute in parallel

```
async function f1() {
    const [valueA, valueB, valueC] = await Promise.all([functionA(), functionB(), functionC()]);

    return valueA + valueB + valueC;
}
```


## async/await with array iteration

### map

```
function asyncThing (value) {
  return new Promise((resolve, reject) => {
    setTimeout(() => resolve(value), 100)
  })
}

async function main () {
  return [1,2,3,4].map(async (value) => {
    const v = await asyncThing(value)
    return v * 2
  })
}

main()
  .then(v => console.log(v))
  .catch(err => console.error(err))
```

### filter

```
function asyncThing (value) {
  return new Promise((resolve, reject) => {
    setTimeout(() => resolve(value), 100)
  })
}

async function main () {
  return [1,2,3,4].filter(async (value) => {
    const v = await asyncThing(value)
    return v % 2 === 0
  })
}

main()
  .then(v => console.log(v))
  .catch(err => console.error(err))
```

### reduce

```
function asyncThing (value) {
  return new Promise((resolve, reject) => {
    setTimeout(() => resolve(value), 100)
  })
}

async function main () {
  return [1,2,3,4].reduce(async (acc, value) => {
    return await acc + await asyncThing(value)
  }, Promise.resolve(0))
}

main()
  .then(v => console.log(v))
  .catch(err => console.error(err))
```
