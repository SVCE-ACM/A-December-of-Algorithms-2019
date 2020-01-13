{- December 26 - Build The Tower -}

import           Data.List

-- Tells the number of operations needed to build a tower out of given
-- compartments
buildTower :: [Integer] -> Integer
buildTower compartments =
    let
        -- Tower can't be taller than any of the compartments
        maxCompHeight  = maximum compartments
        compLength     = toInteger $ length compartments
        -- Tower can't be wider than length of compartments
        maxTowerHeight = max maxCompHeight (compLength `div` 2 + 1)
    in  tryFit maxTowerHeight compartments

tryFit :: Integer -> [Integer] -> Integer
tryFit towerHeight comps =
    let t        = tower towerHeight
        towerLen = length t
        cs       = take towerLen $ dropWhile (== 0) comps
    in  if fits towerHeight comps 0
            then (sum comps) - (sum t)
            else tryFit (towerHeight - 1) comps -- Try with smaller tower

-- Check if tower of given height fits somewhere inside compartments
fits :: Integer -> [Integer] -> Int -> Bool
fits towerHeight comps dropped =
    let t        = tower towerHeight
        towerLen = length t
        cs       = take towerLen $ dropWhile (== 0) $ drop dropped comps
    in  if length cs < towerLen
            then False
            else if and $ zipWith (<=) t cs
                then True
                else fits towerHeight comps (dropped + 1)

-- Generate tower with max height of peak
tower :: Integral a => a -> [a]
tower peak = [1 .. (peak)] ++ reverse [1 .. (peak - 1)]

cmp1 = [1, 2, 1] -- ops 0
cmp2 = [1, 1, 2, 1] -- ops 1
cmp3 = [1, 2, 6, 2, 1] -- ops 3
cmp4 = [0, 1, 3, 3, 2, 3] -- ops 3
cmp5 = [0, 1, 0, 1, 2, 1] -- ops 1
cmp6 = [2, 2, 2, 1] -- ops 3

examples :: [[Integer]]
examples = [cmp1, cmp2, cmp3, cmp4, cmp5, cmp6]

solve :: [Integer] -> IO ()
solve compartments = do
    putStrLn $ "Compartments: " ++ show compartments
    putStrLn $ "Operations needed: " ++ show (buildTower compartments)

main = do
    mapM_ solve examples
