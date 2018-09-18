
[Get started](https://tour.go-zh.org/moretypes/1)

golang doesn't support implicit type coercion by default, user need to transmit variable types manually

c := 3 + 4i  complex128

const Pi = 3.14159   constant variable

capitalized attributes mean that they are exported, while attributes starting with lowercase are not

switch without condition is like a if-else-elseif block, but with better layout

defer postpone command until its function call ends

defer uses stack, deferred commands will be executed in an order or last in first out

Newton method to get square root  
`z` a random assumption  
`z -= (z*z - x) / (2*z)`

Until certain iterations or `abs(x*x - z*z)` is small enough.


*struct object pointer* can access to struct elements in the form of `pointer.element_name`

```
v := Vertex{3, 4}
p := &x
p.X = 123
fmt.Println(p.X)
```

fixed length array `[n]T` size n of type T elements  
`var a [10]int8`

**Slice** variable length array, slice `[]T` type T slice

`var a []int = nums[1:11]`  right bound open  
array slice doesn't create new value objects, any changes to slice elements is made to the original array

array size functions, `len` the number of element array contains, `cap` the maximum number of elements array can have

