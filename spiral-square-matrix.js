/*
Make a function that creates a square matrix/array 
of incrementing integers in a spiral given the size of a square side

example:
____
1

[[1]]
____

2

1 2
4 3
____

3

1 2 3
8 9 4
7 6 5
____

4

1  2  3  4 
14 15 16 5
13 20 17 6
12 19 18 7
11 10  9 8
*/

function printSpiralSquare(n) {
  let m = [];
  let cnt = 1;

  // init
  for (let i = 0; i < n; i++) {
    let l = [];
    for (let j = 0; j < n; j++) {
      l.push("");
    }
    m.push(l);
  }

  // assignment
  for (let loopCnt = 0; loopCnt < n / 2; loopCnt++) {
    let i = 0;
    let j = 0;
    // step 1, left-right
    i = 0 + loopCnt;
    for (j = 0 + loopCnt; j <= n - (1 + loopCnt); j++) {
      m[i][j] = cnt;
      cnt++;
    }

    // step 2, up-down
    j = n - (1 + loopCnt);
    for (i = 1 + loopCnt; i <= n - (1 + loopCnt); i++) {
      m[i][j] = cnt;
      cnt++;
    }

    // step 3, right-left
    i = n - (1 + loopCnt);
    for (j = n - (2 + loopCnt); j >= 0 + loopCnt; j--) {
      m[i][j] = cnt;
      cnt++;
    }

    // step 4, bottom-up
    j = 0 + loopCnt;
    for (i = n - (2 + loopCnt); i >= 1 + loopCnt; i--) {
      m[i][j] = cnt;
      cnt++;
    }
  }
  return m;
}

console.log(printSpiralSquare(9));
