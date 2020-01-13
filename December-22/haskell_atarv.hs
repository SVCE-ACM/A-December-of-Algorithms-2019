{- December 22 - Alternating Balls -}

import           Data.List

data Ball = B | R deriving (Show, Read, Eq)

altBalls :: Eq a => [a] -> [Int]
altBalls balls =
    let subrows = filter (not . null) $ tails balls
    in  map (longestAltSequence) subrows

longestAltSequence :: Eq a => [a] -> Int
longestAltSequence s = altSeq s 1
  where
    altSeq []  count = count
    altSeq [_] count = count
    altSeq (x : xs) count =
        if x /= head xs then altSeq xs (count + 1) else count

main = do
    putStrLn "Enter ball sequence (eg. [B,B,R,R]):"
    balls <- readLn :: IO [Ball]
    putStrLn "Longest alternating sequences for subrows: "
    print $ altBalls balls
