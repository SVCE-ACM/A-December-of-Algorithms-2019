{- December 7 - Queued up -}
import           Prelude
import           Control.Monad

newtype Queue a = Queue [a] deriving (Show)
type Patient = (Int, String)

-- First element to satisfy predicate p is transferred to head of queue
jumpQueue :: (a -> Bool) -> Queue a -> Queue a
jumpQueue p (Queue q) =
    case break p q of
        (xs, y:ys) -> Queue (y:xs ++ ys)
        _ -> Queue q

main :: IO ()
main = do
    putStrLn "Enter number of patients:"
    nPatients <- readLn :: IO Int
    putStrLn "Enter patients names/IDs (line by line):"
    patientIds <- replicateM nPatients getLine :: IO [String]
    let queue = Queue $ zip [1 ..] patientIds :: Queue Patient
    print queue
    putStrLn "Enter k (id of patient let in first):"
    k <- getLine
    print $ jumpQueue (\(_, p) -> p == k) queue
