{- December 29 - Vigenere Cipher -}

import           Data.Char

-- Decipher Vigenère Cipher text
decipher :: String -> String -> String
decipher cipher kstream = zipWith
    (\c k -> (chr . (+ ord 'A')) $ (numOrder c - numOrder k) `mod` 26)
    cipher
    kstream

-- Numeric order starting with A = 1
numOrder :: Char -> Int
numOrder char = ord char - ord 'A' + 1

-- Turn keyword into a keystream
keystream :: String -> String
keystream key = cycle key

main = do
    putStrLn "(All text must be upper case and sans whitespace)"
    putStrLn "Enter keyword:"
    key <- getLine
    putStrLn "Enter ciphered text:"
    cipheredText <- getLine
    let kstream = take (length cipheredText) $ keystream key
    putStrLn $ "Keystream: " ++ kstream
    putStrLn $ "Message: " ++ (decipher cipheredText kstream)
