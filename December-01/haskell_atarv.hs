-- December 1 - Sevenish Number
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

-- Calculate how many powers are needed to be able to calcualate the number in
-- index i
powersNeeded :: (Num a, Ord a) => a -> Int
powersNeeded i = (1+) $ length $ takeWhile (<i) $ map (\n -> (2^n)-1) [1..]

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