{- December 9 - One to One? -}
import           Prelude
import           Data.Set                       ( Set
                                                , delete
                                                , size
                                                , elemAt
                                                , member
                                                , fromList
                                                )
import           Language.Haskell.Interpreter

oneToOne :: (Ord a, Ord b) => (a -> b) -> Set a -> Set b -> String
oneToOne f set targetSet =
    let param  = elemAt 0 set
        result = f param
    in  case (size set, size targetSet) of
            (0, 0)    -> "bijective"
            (0, _)    -> "one to one, not bijective"
            otherwise -> if result `member` targetSet
                then oneToOne (f) (delete param set) (delete result targetSet)
                else "not one to one"


readIntSet :: IO (Set Int)
readIntSet = getLine >>= (return . fromList . map (read) . words)

main :: IO ()
main = do
    putStrLn "Enter set A:"
    setA <- readIntSet
    print setA
    putStrLn "Enter set B:"
    setB <- readIntSet
    print setB
    putStrLn "Function (Int -> Int), eg. \\x -> x^2+3"
    expr <- getLine
    r    <- runInterpreter $ do
        setImports ["Prelude"]
        interpret expr (as :: Int -> Int)
    case r of
        Left  err -> print err
        Right f   -> putStrLn $ oneToOne (f) setA setB
