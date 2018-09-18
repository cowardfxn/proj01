
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

