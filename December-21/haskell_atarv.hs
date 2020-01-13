{- December 21 - Marching Partners -}

import Data.List

marchingPartners :: Int -> [Int] -> Int -> Int
marchingPartners n heights maxDelta =
    countPairs (sort heights) maxDelta 0

countPairs :: [Int] -> Int -> Int -> Int
countPairs [] _ pairs = pairs
countPairs [x] _ pairs = pairs
countPairs (x:y:xs) maxDelta pairs =
    if abs (x - y) <= maxDelta
        then countPairs xs maxDelta (pairs+1)
        else countPairs (y:xs) maxDelta pairs

main = do
    putStrLn "Enter student heights separated with space:"
    heights <- getLine >>= return . map (read) . words :: IO [Int]
    putStr "Enter max deviation for marching partner heights: "
    d <- readLn :: IO Int
    putStr "Maximum number of possible pairs: "
    print $ marchingPartners (length heights) heights d