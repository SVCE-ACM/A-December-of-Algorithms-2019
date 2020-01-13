{- December 16 - Casino Royale -}

import           Data.List
import           Data.Maybe

data Suit = Hearts | Diamonds | Clubs | Spades deriving (Show, Eq, Ord)
type Card = (Int, Suit)

suitFromString :: Char -> Maybe Suit
suitFromString s = case s of
    'h'       -> Just Hearts
    'd'       -> Just Diamonds
    'c'       -> Just Clubs
    's'       -> Just Spades
    otherwise -> Nothing

faceValueFromString :: String -> Int
faceValueFromString f = case f of
    "a"       -> 14
    "k"       -> 13
    "q"       -> 12
    "j"       -> 11
    otherwise -> read f :: Int

cardFromString :: String -> Maybe Card
cardFromString s =
    let face = faceValueFromString $ init s :: Int
        suit = suitFromString $ last s
    in  if isJust suit && (face <= 14 && face >= 2)
            then Just (face, fromJust suit)
            else Nothing

parseHand :: String -> [Card]
parseHand hand =
    let cards = nub $ catMaybes $ map (cardFromString) $ words hand
    in  if (length cards) == 5 then cards else fail "Error parsing hand"

cardValues :: [Card] -> [Int]
cardValues = map (fst)

cardSuits :: [Card] -> [Suit]
cardSuits = map (snd)

isStraight :: [Card] -> Bool
isStraight hand =
    let
        valueSequence = sort $ cardValues hand
        seqMin        = head valueSequence
        lowAceSequence =
            sort $ map (\x -> if x == 14 then 1 else x) valueSequence
    in
        valueSequence == [seqMin .. (seqMin + 4)] || lowAceSequence == [1 .. 5]

isFlush :: [Card] -> Bool
isFlush hand = (length $ nub $ cardSuits hand) == 1

handKind :: [Card] -> Int
handKind hand = last $ sort $ map (length) $ group $ sort $ cardValues hand

isTwoPair :: [Card] -> Bool
isTwoPair hand = case sort $ map (length) $ group $ sort $ cardValues hand of
    [1, 2, 2] -> True
    otherwise -> False

isFullHouse :: [Card] -> Bool
isFullHouse hand = case sort $ map (length) $ group $ sort $ cardValues hand of
    [2, 3]    -> True
    otherwise -> False

handRanking :: [Card] -> String
handRanking h | isStraight h && isFlush h = "straight-flush"
              | (handKind h) == 4         = "four-of-a-kind"
              | isFullHouse h             = "full-house"
              | isFlush h                 = "flush"
              | isStraight h              = "straight"
              | (handKind h) == 3         = "three-of-a-kind"
              | isTwoPair h               = "two-pair"
              | (handKind h) == 2         = "one-pair"
              | (handKind h) == 1         = "high-card"
              | otherwise                 = "invalid"

main :: IO ()
main = do
    putStrLn "Enter poker hand:"
    handLine <- getLine
    let hand = parseHand handLine
    if null hand then fail "Invalid hand" else putStrLn $ handRanking hand
