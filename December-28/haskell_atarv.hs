{- December 28 - Toss a coin to your Witcher -}

import           Data.Set                       ( Set
                                                , fromList
                                                , member
                                                , singleton
                                                , insert
                                                )

formGroups :: [[Int]] -> [Set Int]
formGroups people = formGroups' (zip [0 ..] people) []
  where
    formGroups' :: [(Int, [Int])] -> [Set Int] -> [Set Int]
    formGroups' [] groups = groups
    formGroups' ((n, ppl) : xs) groups =
        let friendsOfN =
                    filter (not . (== 0)) $ drop n $ zipWith (*) [1 ..] ppl
            friendsNotInGroups =
                    filter (not . (flip any groups . member)) friendsOfN
        in  formGroups'
                xs
                (if null friendsNotInGroups
                    then groups
                    else groups ++ [fromList friendsNotInGroups]
                )

exampleInput :: [[Int]]
exampleInput = [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 1]]

plural :: (Eq a, Num a, Show a) => a -> String -> String
plural n s | n == 0    = "No " ++ s ++ " is "
           | n == 1    = "An " ++ s ++ " is "
           | otherwise = show n ++ " " ++ s ++ "s are "

main = do
    putStrLn "Input:"
    print exampleInput
    let groupSizes = map (length) $ formGroups exampleInput
    putStrLn $ "Number of groups: " ++ show (length groupSizes)
    putStrLn
        $  (plural (length $ filter (== 1) groupSizes) "Assassin")
        ++ "present"
