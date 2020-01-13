{- December 13 - Toggling Switches -}

-- As this uses list comprehension it's time complexity is probably O(n)
nSwitchesOn :: Integer -> Int
nSwitchesOn n = length [ x | x <- [1 .. n], x ^ 2 <= n ]

-- Constant time complexity implementation
constantSwitchesOn :: Integer -> Int
constantSwitchesOn n = (floor . sqrt . fromIntegral) n

main = do
    putStrLn "Enter number of switches:"
    n <- readLn :: IO Integer
    putStrLn
        $  "Number of switches on at round "
        ++ (show n)
        ++ ": "
        ++ (show $ constantSwitchesOn n)
    main
