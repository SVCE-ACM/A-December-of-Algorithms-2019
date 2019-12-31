{- December 20 - 100 days of summer -}

import           Data.List
import           Text.Printf

-- This is the naive solution with time complexity of O(n!)
travellingSalesman :: (Num a, Ord a) => [[a]] -> a
travellingSalesman distances =
    (minimum . map (routeDistances distances . (++ [0])) . permutations)
        [1 .. (length distances) - 1]

routeDistances :: (Num a, Ord a) => [[a]] -> [Int] -> a
routeDistances distances cities = dist' 0 cities
  where
    dist' _ [] = 0
    dist' from (to : remaining) =
        (distances !! from !! to) + dist' to remaining

-- modify this or make the function call with another matrix to change the
-- outcome
exampleDistances :: [[Int]]
exampleDistances =
    [[0, 40, 10, 30], [40, 0, 20, 10], [10, 20, 0, 50], [30, 10, 50, 0]]

printMatrixRow :: [Int] -> IO ()
printMatrixRow r = sequence_ $ (map (printf "%4d") r) ++ [putStrLn ""]

printMatrix :: [[Int]] -> IO ()
printMatrix = mapM_ (printMatrixRow)

main = do
    putStrLn "For distance matrix: "
    printMatrix exampleDistances
    putStr "The shortest distance is: "
    print $ travellingSalesman exampleDistances
