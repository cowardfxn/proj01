
## postgresql
*incremental development*
methodology module and data extend with development, dynamic table type fits better
*ACID*
Atomic, Consistent, Isolated, Durabled  features of postgresql model

[Original article](https://github.com/lukehoban/es6features#readme)  
[More Resources](https://github.com/rse/es6-features)

## ES2015
ES2015 AKA ES6

##### arrow
new function declaration syntax with `=>`, unlike *function*, arrows share the same lexical this as their surrounding code

```
let station = {
    name: "new television",
    channel: 21,
    broadcast(show) {
        return `Welcome to ${show} at channel ${this.channel}`;
    },
    getChannel() {
        return this.channel
    }
}

station.getChannel() == 21
```

##### template string
use "\`" at both ends to imply this is a template string, use`${varName}` to include variable value

```
let a = 100;
let str1 = `Value of a is ${a}`;
```

##### class
support define class, classes support prototype-based inheritance, super calls, instance and static methods and constructors


##### destructuring
allows binding using pattern matching, with support for matching array and objects, is similar to standard object lookup `foo["bar"]`, product nothing when not found
destructuring is fail-soft, if the assignation failed, the original variable value won't be affected

```
> let [b, ,c] = [1,2,3,4,5,6]
> b
1
> c
3
> let {a1: a, b1:{b11:b}, c1:[c2, c3]} = {a1: "a1frf", b1:{b11:453}, c1:[4,5,6,7,8,9]}
undefined
> a
'a1frf'
> b
453
> c2
4
> c3
5
> [a=1] = [];
[]
> a
1
> [a] = [];
[]
> a
```

##### default+rest+spread
support default argument value, use "..." to represent all the rest arguments, use "..." at function call to spread object values to function arguments

```
// default
function add(x, y=15) {
    return x + y;
}

// rest
function f(x, ...y) {
    return x * y.length;
}

f(4, "234", [1,2,3]) === 8

// spread
f(...[5, 6, 7, 8]) === 15
```

##### let+const
block-scoped binding constructs, *let* is used for declaring scoped variable and can not be redeclared, *const* is used to define static variable which can not be changed after declaration

##### new iterator
`for...of...`
can only be used on array, to iterate all the elements

```
let arr1 = [1,2,3,4,5,6];
for (let e of arr1) {
    console.log(e);
}
```

##### generator
defined with `function*` and `yield`, can also be used to enable `await`

##### proxy
define object attributes directives

```
const target = {},
    handler = {
        get: (receiver, name) => {
            return `hello, ${name}`
        }
    };

let p = new Proxy(target, handler);
p.world === "hello, world"
```


##### tail calls
calls in tail position are guaranteed to not grow the stack unboundedly, make recursive algorithms safe in the face of unbounded inputs

```
function factorial(n, acc=1) {
    if (n < 2) {
        return n;
    }
    return n * factorial(n - 1);
}
```

