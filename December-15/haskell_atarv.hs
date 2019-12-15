{- December 15 - Intruder Alert -}

ingredientCombinations :: Int -> [String]
ingredientCombinations n = ingredients n n "" []
  where
    ingredients 0 0 combination combinations = combinations ++ [combination]
    ingredients amountA amountB combination combinations =
        let
            addIngredientA =
                (ingredients (amountA - 1)
                             amountB
                             (combination ++ "A")
                             combinations
                )
            addIngredientB =
                (ingredients amountA
                             (amountB - 1)
                             (combination ++ "B")
                             combinations
                )
        in
            case (amountA, amountB, amountA `compare` amountB) of
                (0, _, LT) -> combinations ++ addIngredientB
                (_, _, LT) -> combinations ++ addIngredientA ++ addIngredientB
                (_, _, EQ) -> combinations ++ addIngredientA
                (_, _, GT) -> combinations ++ addIngredientA

main :: IO ()
main = do
    putStr "Quantity of A (in grams): "
    g <- readLn :: IO Int
    let combinations = ingredientCombinations g
    putStr "Combinations: "
    print combinations
