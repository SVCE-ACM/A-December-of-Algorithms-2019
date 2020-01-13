{- December 10 - Count The Cookies -}
import Prelude

-- Returns number of cookies that could be bought with given amount of credits,
-- cookie jar cost, jars to return for a free cookie
cookieCount :: Integral t => t -> t -> t -> t
cookieCount credits cost jarsForCookie = 
    countCookies credits cost jarsForCookie 0
    where 
        countCookies n p c jars =
            let
                (boughtCookies, creditsLeft) = divMod n p
                (cookiesFromJars, jarsLeft) = divMod (jars + boughtCookies) c
                totalCookies = boughtCookies + cookiesFromJars
            in if n < p && jars < c
                    then totalCookies
                    else totalCookies 
                         + (countCookies creditsLeft p c (jarsLeft + cookiesFromJars))

main :: IO ()
main = print $ cookieCount 15 3 2