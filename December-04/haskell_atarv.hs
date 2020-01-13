{- December 4 - Dr. Bruce Banner's H-Index -}
import           Prelude
import           Data.List

-- Given list of citation counts tells researcher's h-index
hIndex :: [Int] -> Int
hIndex citations =
    foldr
            (\c maxH ->
                if head c >= maxH && length c >= head c then head c else maxH
            )
            0
        $ (filter (not . null) . tails . sort) citations

main :: IO ()
main = do
    putStrLn "Enter list of citation counts"
    citations <- readLn :: IO [Int]
    putStrLn $ "Researcher's h-index is " ++ show (hIndex citations)

