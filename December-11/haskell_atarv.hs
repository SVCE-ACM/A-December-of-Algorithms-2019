{- December 11 - Is This A Valid Email Address -}
-- Fulfills only the limited email syntax specification from the assignment.
-- Also, regex is not part of the base package, so I used a different approach.
import           Prelude
import           Data.Set
import           Data.Text                     as T

alphabets :: [Char]
alphabets = ['A' .. 'Z'] ++ ['a' .. 'z']

digits :: [Char]
digits = ['0' .. '9']

domainChars :: Set Char
domainChars = fromList $ alphabets

localChars :: Set Char
localChars = fromList $ alphabets ++ digits ++ ['_', '-', '.']

-- Accepted top level domain
tld :: Text
tld = pack "com"

isValidLocal :: Text -> Bool
isValidLocal = T.all (`member` localChars)

isValidDomain :: Text -> Bool
isValidDomain = T.all (`member` domainChars)

isValidEmail :: Text -> Bool
isValidEmail address = case T.split (== '@') address of
    [local, domain] -> isValidLocal local && 
                            case T.split (== '.') domain of
                                [d, t]    -> isValidDomain d && t == tld
                                otherwise -> False
    otherwise -> False

main :: IO ()
main = do
    putStrLn "Enter email to check:"
    email <- getLine
    if email == ""
        then return () -- Exit program if line empty
        else if isValidEmail (pack email)
            then do
                putStrLn "is valid"
                main
            else do
                putStrLn "is invalid"
                main
