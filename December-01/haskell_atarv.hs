{- 
    December 1 - Sevenish Number
    Run the program: 
        ghci haskell_atarv.hs 
        main
            (or call the function directly: sevenishNumber 7)
-}
module Main where
import Prelude
import Data.List

-- Infinite sequence of powers of seven
powersOfSeven :: Num a => [a]
powersOfSeven = iterate (*7) 1

-- Generate all possible sums of the numbers in list
generateAllSums :: Num a => [a] -> [a]
generateAllSums [] = []
generateAllSums list = map sum $ filter (not . null) $ subsequences list

-- Calculate the nth sevenish number
sevenishNumber :: Num a => Int -> a
sevenishNumber n = 
    map sum (filter (not . null) $ subsequences $ take n powersOfSeven) !! (n-1)

main :: IO ()
main = do
    putStrLn "Which seventh number to calculate?"
    n <- readLn :: IO Int
    let sevenish = sevenishNumber n :: Integer
    putStrLn $ show n ++ ": " ++ show sevenish