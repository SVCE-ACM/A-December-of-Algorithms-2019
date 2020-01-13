{- 
    December 2 - Is this a valid credit card number?
-}
import           Prelude                 hiding ( odd
                                                , even
                                                )
import           Data.Char

-- Partition elements in odd indexes (starting with 1) to first element of tuple
-- and elements in even indexes to second
partitionOddsAndEvens :: [a] -> ([a], [a])
partitionOddsAndEvens []       = ([], [])
partitionOddsAndEvens (x : xs) = partitionAlternateOdd xs ([x], [])
  where
    partitionAlternateOdd [] (odd, even) = (odd, even)
    partitionAlternateOdd (y : ys) (odd, even) =
        partitionAlternateEven ys (odd, even ++ [y])
    partitionAlternateEven [] (odd, even) = (odd, even)
    partitionAlternateEven (y : ys) (odd, even) =
        partitionAlternateOdd ys (odd ++ [y], even)

-- Sum of digits (characters)
sumDigits :: Foldable t => t Char -> Int
sumDigits = foldl (\acc cur -> acc + digitToInt cur) 0

-- Checks if given credit card number is valid
validateCreditCardNumber :: Integer -> Bool
validateCreditCardNumber num =
    let (oddDigits, evenDigits) = partitionOddsAndEvens $ show num
        oddDigitSum             = sumDigits oddDigits
        evenDigitsDoubled       = map (show . (* 2) . digitToInt) evenDigits
        doubledDigitsSummed     = map sumDigits evenDigitsDoubled
        evenLastSum             = sum doubledDigitsSummed
    in  '0' == last (show $ oddDigitSum + evenLastSum)

main :: IO ()
main = do
    creditNumber <- readLn :: IO Integer
    let isValid = validateCreditCardNumber creditNumber
    putStr $ show creditNumber
    if isValid
        then putStr " passes the test\n"
        else putStr "doesn't pass the test\n"

