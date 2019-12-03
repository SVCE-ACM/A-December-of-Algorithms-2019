{- 
    December 3 - The Decimation
-}
import           Prelude

-- Checks that list is sorted in ascending order
isSorted :: Ord a => [a] -> Bool
isSorted []           = True
isSorted [_         ] = True
isSorted (x : y : xs) = x <= y && isSorted (y:xs)

-- Snap (remove) the latter half of list until it is sorted
snap :: Ord a => [a] -> [a]
snap list = if isSorted list
    then list
    else snap $ fst $ splitAt (length list `div` 2) list


main :: IO ()
main = do
    let list1 = [1, 2, 3, 4, 5] :: [Integer]
    print list1
    putStrLn "After snap: "
    print $ snap list1
    let list2 = [1, 2, 3, 4, 3] :: [Integer]
    putStrLn "After snap: "
    print $ snap list2
    let list3 = "Hello there!"
    putStrLn "After snap: "
    print $ snap list3

