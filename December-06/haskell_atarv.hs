{- December 6 - Fibonacci Prime Number Generation -}
import Prelude

-- With help from Haskell Wiki
-- Generates infinite list of Fibonacci numbers
fibs :: [Integer]
fibs = scanl (+) 0 (1:fibs)

-- From SO, modified
-- Tests primality of k
isPrime :: Integer -> Bool
isPrime k = (k > 1) && null [ x | x <- [2..k - 1], k `mod` x == 0]

main :: IO ()
main = do
    putStrLn "Enter the value for (n)"
    n <- readLn :: IO Int
    let primeFibs = filter isPrime fibs
    print $ take n primeFibs
