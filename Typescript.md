# Typescript

Typescript expects you to declare before you could use a variable

Always use `===` and `!==` since `==` performs type coercion by default

null and undefined

 - Something hasn't been initialized: *undefined*
 - Something is currently unavailable: *null*

In **strict mode** if you use `foo` and `foo` is *undefined*, you get a `ReferenceError` exception rather than continuing with vaiable `foo` being *undefined*.

##### Node style callbacks
Callback functions with error as first parameter, the program is treated as no exception if error is null.

```
(err, data) => {
  if (err) {
    // error handling
  } else {
    // normal branch
  }
}
```

Typescript team don't use *null* and they prefer using *undefined*, while Node style code uses *null* for Error arguments. This may result in errors when referencing js libraries.

`this` is commonly referred to as the **calling context**, not just inside function scope.  
To disconnect `this` in a class from the calling context, use the arrow function syntax.

If you want `this` to be the calling context as libraries like jquery, underscore, mocha and others expect, you should not use arrow function, just use a `function` declaration.


Closure enables inner functions access variables outside of its scope even if outside function is end. *Global variable reference in memory?*

Javascript has only one number type, a double-precision 64-bit `Number`.

class can have static attributes, and public, protected, private accessibility

accessible on | `public` | `protected` | `private`
:---- | :---- | :---- | :----
class | yes | yes | yes
class children | yes | yes | no
class instance | yes | no | no

class can be interited

class constructor is optional

Rest parameters  
`...argumentName` to group arguments

Functions create a new variable scope in JavaScript

A `const` is block scoped like `let`

```
const foo = 123;
if (true) {
  const foo = 456;  // a new const variable in if block
}
```

Array destructuring can be used to swap values

```
[b, a] = [a, b]
```

Object spread  
functions similar to `Object.assign`, what comes first is 'overwridden' by what comes later.

```
const point2D = {x: 2, y: 3};
const point3D = {...point2D, z: 4};
```

`for...of` iterates over array elements