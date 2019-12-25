{- December 24 - Find the list -}

findList :: Eq a => [a] -> [a]
findList elems = findList' elems 1
  where
    findList' elems len =
        let count    = length elems
            tryElems = take len $ everyNth 3 elems
        in  if elems == (take count $ reenasAlgorithm $ cycle $ tryElems)
                then tryElems
                else findList' elems (len + 1)

everyNth :: Int -> [a] -> [a]
everyNth n [] = []
everyNth n xs = head xs : everyNth n (drop n xs)

reenasAlgorithm :: [a] -> [a]
reenasAlgorithm [] = []
reenasAlgorithm xs = take 3 xs ++ reenasAlgorithm (drop 1 xs)

example :: [Int]
example = [54, 65, 44, 65, 44, 89, 44, 89, 54, 89]

main = do
    putStrLn "Output from Reena's algorithm:"
    print example
    putStrLn "Elements of original list:"
    print $ findList example
