{- December 18 - Your Password is too WEAK -}
-- to run multithreaded:
--      stack ghci haskell_atarv.hs --ghci-options='+RTS -N -RTS'

import           Data.Time.Clock
import           Data.Char
import           Control.Concurrent
import           Control.Monad                  ( forM_ )
import           GHC.Conc                       ( getNumProcessors )

nextAsciiString :: String -> String
nextAsciiString []       = " "
nextAsciiString (x : xs) = case ord x of
    126       -> (chr 32) : (nextAsciiString xs)
    otherwise -> chr (succ $ ord x) : xs

bruteForce :: Char -> String -> String
bruteForce c pass =
    until (== pass) (nextAsciiString) (replicate (length pass) c)

main = do
    putStr "Enter password: "
    password  <- getLine
    nThreads  <- getNumProcessors
    start     <- getCurrentTime
    isCracked <- newEmptyMVar :: IO (MVar Bool)
    forM_
        (take nThreads $ iterate (+ ((126 - 32) `div` nThreads)) 32)
        (\x -> forkIO $ do
            let value = password == bruteForce (chr x) password
            putMVar isCracked $! value
        )
    takeMVar isCracked
    stop <- getCurrentTime
    putStr "Time taken: "
    print $ diffUTCTime stop start
