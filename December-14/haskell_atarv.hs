{- December 14 - A Wordplay with Vowels and Consonants -}
import           Data.Set                       ( fromList
                                                , member
                                                , Set
                                                )
import           Data.List

data Player = A | B

-- Vowels in English
vowels :: Set Char
vowels = fromList "aeiou"

isVowel :: Char -> Bool
isVowel c = c `member` vowels

-- Generates substrings of string
substrings :: String -> [String]
substrings s = substrings' s []
  where
    substrings' [] subs = subs
    substrings' (x : xs) subs =
        substrings' (xs) $ subs ++ (filter (not . null) $ inits (x : xs))

-- First is substrings starting with a vowel (player A), second starting with any other character (player B)
substringsByPlayer :: String -> ([String], [String])
substringsByPlayer s = partition (isVowel . head) $ substrings s

winnerAndScore :: String -> (Maybe Player, Int)
winnerAndScore s =
    let (substringsA, substringsB) = substringsByPlayer s
    in  case (length substringsA) `compare` (length substringsB) of
            LT -> (Just B, length substringsB)
            GT -> (Just A, length substringsA)
            EQ -> (Nothing, length substringsA)

main = do
    putStrLn "Enter string:"
    s <- getLine
    case winnerAndScore s of
        (Nothing, score) -> putStrLn $ "It's a tie with score " ++ show score
        (Just A , score) -> putStrLn $ "Winner is A with score " ++ show score
        (Just B , score) -> putStrLn $ "Winner is B with score " ++ show score
