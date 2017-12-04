Promise

> A promise is an abstraction for asynchronous programming. It's an object that proxies for the return value or the exception thrown by a function that has to do some asynchronous processing.

### Standard promise
```
let promise = doSomethingAsync();
promise.then(onFulfilled, onRejected);
```

The point of Promise is that the `then` method of a promise object also returns a promise object. In this way, the then process can be chained.

### Error handling
Other than writing both `onFulfilled` and `onRejected` function in one `then` call, it can also be written like this:

```
...
promise
    .then(onFulFilled)
    .then(undefined, onRejected)
```

If an error occurs in the process in promise, the first `then` has undefined as `onRejected` function, the error will be transmitted to the second `then` function, and taken care of by the `onRejected` function defined there

Meanwhile, the grammer `.then(undefined, onRejected)` has a shorthand: `.catch(onRejected)`, so a promise call with error handling like try/catch implemented can be written like this:

```
...
promise.
    .then(onFulFilled)
    .catch(onRejected)
```

Libraries like **bluebird** can help to build promise from ordinary Node style callback function.
