{- December 8 - Cheating Probability -}
import           Prelude
import           Data.List
import           Text.Printf
import           Control.Monad

data Neighbor = Front | Behind | Side | Diagonal deriving (Enum, Show)

-- Get student rows from user
askStudentRows :: [[String]] -> IO [[String]]
askStudentRows rows = do
    row <- getLine :: IO String
    if row == "" then return rows else askStudentRows $ rows ++ [words row]

-- Calculate (row, col) positions for each student
getStudentPositions :: [[String]] -> [(Int, Int, String)]
getStudentPositions rows =
    let columnsNumbered = map (zip [1 ..]) rows
        positions =
                map (\(rownum, cols) -> map (\(coln, p) -> (rownum, coln, p)) cols)
                    $ zip [1 ..] columnsNumbered
    in  concat positions

-- Checks if second student is neighbor of the first
neighbor :: (Int, Int, String) -> (Int, Int, String) -> Maybe Neighbor
neighbor (rowA, colA, _) (rowB, colB, _) =
    case (rowA - rowB, abs $ colA - colB) of
        (0 , 0)   -> Nothing -- No student is neighbor of themselves
        (-1, 0)   -> Just Behind
        (1 , 0)   -> Just Front
        (0 , 1)   -> Just Side
        (-1, 1)   -> Just Diagonal
        (1 , 1)   -> Just Diagonal
        otherwise -> Nothing

-- Calculate cheating probability from neighbors relative position
cheatingRelation :: Maybe Neighbor -> Double
cheatingRelation neighbor = case neighbor of
    Just Front    -> 0.3
    Just Behind   -> 0.2
    Just Side     -> 0.2
    Just Diagonal -> 0.025
    otherwise     -> 0.0

-- Cheating probability for one student
cheatingProbability :: (Int, Int, String) -> [(Int, Int, String)] -> (Int, Int, Double)
cheatingProbability (row, col, exam) students =
    let probability =
                sum $ map (cheatingRelation . neighbor (row, col, exam)) $ filter
                    (\(r, c, e) -> exam == e)
                    students
    in  (row, col, probability)

-- Cheating probabilities of all students
probabilities :: [(Int, Int, String)] -> [(Int, Int, Double)]
probabilities students = map (flip cheatingProbability students) students

-- Form student rows again with their positions (also discarding the position numbers)
positionsToRows :: [(Int, Int, a)] -> [[a]]
positionsToRows probs =
    let rows = groupBy (\(rowA, _, _) (rowB, _, _) -> rowA == rowB) probs
    in  map (map (\(_, _, p) -> p)) rows


-- Print one row of doubles
printRow :: [Double] -> IO ()
printRow row = sequence_ $ flip (++) [putStrLn ""] $ map (printf "%.3f ") row

-- Print each row
printRows :: [[Double]] -> IO ()
printRows rows = sequence_ $ map (printRow) rows

main :: IO ()
main = do
    putStrLn "Enter student rows (finish with empty line)"
    rows <- askStudentRows []
    printRows $ (positionsToRows . probabilities . getStudentPositions) rows
