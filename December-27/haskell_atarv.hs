{- December 27 - Spiralling -}

import           Data.List

rotateLeft :: [[a]] -> [[a]]
rotateLeft = reverse . transpose

spiral :: [[a]] -> [a]
spiral [x     ] = x
spiral (x : xs) = x ++ spiral (rotateLeft xs)

exampleInput :: [[Int]]
exampleInput = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

getStudentRows :: [[Int]] -> IO [[Int]]
getStudentRows rows = do
    row <- getLine :: IO String
    if row == ""
        then return rows
        else getStudentRows $ rows ++ [map (read) $ words row]

main = do
    putStrLn "Enter student rows:"
    rows <- getStudentRows []
    print $ spiral rows
