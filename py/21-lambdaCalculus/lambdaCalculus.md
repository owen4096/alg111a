# Lambda Calculus

終於了解 Lambda Calculus 在玩些甚麼遊戲了。

基本上就是，一切皆函數，資料結構也是透過函數 (像是 pair, car, cdr 包在 closure 裡面的)

然後，每個函數都只接受一個參數，然後傳回一個值 (也是函數)。

而其中最關鍵的一個函數，就是 if ，定義如下：

> if: λc.λx.λy. c x y 

其語意為 if c then x else y.

然後搭配 true , false 的定義

```
true: λx.λy. x
false: λx.λy. y
```

於是就能定義出 and, or, not 了 ...

```
and: λp.λq. p(q)(p)     # if p then q else p
or : λp.λq. p(p)(q)     # if p then p else q
not: λc. c(FALSE)(TRUE) # if c then false else true
```

## Y-Combinator

由於 if 的定義走兩條路，因此需要 c x y 等參數。

於是要傳入一個函數讓他兩條路都走一遍時，就必須用 x x 的方式傳入

才能執行 f(x)(x) ，這就是 Y-Combinator 的用途。

```
Y = lambda f:\
  (lambda x:f(lambda y:x(x)(y)))\
  (lambda x:f(lambda y:x(x)(y)))
```

