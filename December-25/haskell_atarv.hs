{- December 25 - Naughty Jack -}

import           Data.List
import           Data.Maybe
import           Foreign.Marshal.Utils          ( fromBool )

data Bit = Bit Bool | ParityBit Bool deriving (Eq)

instance Show Bit where
    show b = case b of
        Bit       b -> (show . fromBool) b
        ParityBit b -> (show . fromBool) b ++ "P"

readBit :: String -> Maybe Bit
readBit b = case b of
    "0"  -> Just $ Bit False
    "1"  -> Just $ Bit True
    "0P" -> Just $ ParityBit False
    "1P" -> Just $ ParityBit True
    _    -> Nothing

isParity :: Bit -> Bool
isParity bit = case bit of
    Bit       _ -> False
    ParityBit _ -> True

bitValue :: Bit -> Int
bitValue bit = case bit of
    Bit       True -> 1
    ParityBit True -> 1
    _              -> 0

repairDisks :: [[Maybe Bit]] -> [[Bit]]
repairDisks disks =
    let rows          = map (\row -> repair row disks) [0 .. length disks - 1]
        repairedDisks = map (\n -> map (!! n) rows) [0 .. length disks - 1]
    in  repairedDisks

repair :: Int -> [[Maybe Bit]] -> [Bit]
repair n disks =
    let bits                  = map (!! n) disks
        -- finding parity bit fails if there is none
        ParityBit parityValue = head $ catMaybes $ find (isParity) <$> bits
        bitsum                = sum $ map (bitValue) $ catMaybes bits
    in  if parityValue && even bitsum
         -- missing value is 0
            then map (fromMaybe (Bit False)) bits
         -- missing value is 1
            else map (fromMaybe (Bit True)) bits

printDisks :: (Show a) => [a] -> IO ()
printDisks disks = do
    let annotatedDisks =
            zipWith (\d n -> "Disk " ++ (show n) ++ " " ++ show d) disks [1 ..]
    mapM_ (putStrLn) annotatedDisks

exampleInput :: [String]
exampleInput =
    [ "0 1 1 * 1P"
    , "1 0 1 1P 0"
    , "* 0 0P 0 0"
    , "0 0P * 1 0"
    , "1P * 1 0 *"
    ]

exampleDisks :: [[Maybe Bit]]
exampleDisks = map
    (map (readBit) . words) exampleInput

main = do
    putStrLn "Input:"
    printDisks exampleInput
    putStrLn "\nAfter restoration:"
    printDisks $ repairDisks exampleDisks
