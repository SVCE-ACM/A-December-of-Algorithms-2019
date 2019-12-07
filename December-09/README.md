This program depends on package [hint](http://hackage.haskell.org/package/hint)
so you will need to have it installed.

Installing with `stack`:

```
stack install hint
```

Using the program:

```
> stack runhaskell haskell_atarv.hs
Enter set A:
1 2 3 4
fromList [1,2,3,4]
Enter set B:
1 4 9 16
fromList [1,4,9,16]
Function (Int -> Int), eg. \x -> x^2+3
(^2)
bijective
```
                                     