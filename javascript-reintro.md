# Javascript re-introduction

[Original article](https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript)

Unlike most programming languages, the Javascript language has no concept of input or output.  
It is designed to run as a scripting language in a host environment, and it is the host environment to provide mechanisims for communicating with the outside world.

#### Types of Javascript

 - Number  double-precision 64-bit format IEEE 754 values
 - String  sequences of unicode character
 - Boolean
 - Symbol
 - Object
  * Function
  * Array
  * Date
  * RegExp
 - null  a deliberate none value
 - undefined  a type that indicates an unintialized value


##### Number
`NaN` Not a Number, operating with any number would return a NaN  

`Infinity` infinity, could be judged by `isFinite()` 

##### Two ways of copying objects

```
Object.assign(target, srcObj);
# Or...
let newObj = {... srcObj};
```
