{- December 17 - Subway Surfer -}
{-# OPTIONS_GHC -fwarn-incomplete-patterns #-}

import           Prelude                 hiding ( lines )
import           Data.List               hiding ( lines )
import           Data.Maybe

data Station = Station {name :: String, routes :: [String]} deriving (Show, Eq)

bothWays :: [a] -> [a]
bothWays s = s ++ drop 1 (reverse s)

parseLine :: [String] -> [Station] -> [Station]
parseLine []  stations = stations
parseLine [x] stations = if isJust (find ((== x) . name) stations)
    then parseLine [] (updateStations stations)
    else parseLine [] (addStation stations)
  where
    updateStations = map
        (\a -> if (name a) == x
            then Station { name = x, routes = routes a }
            else a
        )
    addStation = flip (++) [Station { name = x, routes = [] }]
parseLine (x : y : xs) stations = if isJust (find ((== x) . name) stations)
    then parseLine (y : xs) (updateStations stations)
    else parseLine (y : xs) (addStation stations)
  where
    updateStations = map
        (\a -> if (name a) == x
            then Station { name = x, routes = routes a ++ [y] }
            else a
        )
    addStation = flip (++) [Station { name = x, routes = [y] }]

parseStations :: [[String]] -> [Station]
parseStations lines = foldl (flip parseLine) [] (map bothWays lines)

exampleStations = parseStations
    [ [ "Greenwhich"
      , "Suntech"
      , "Marina"
      , "Central"
      , "CityHall"
      , "Bay"
      , "Museum"
      , "RiverFront"
      , "Downtown"
      , "Airport"
      ]
    , ["Park", "Central", "Zoo", "Estate", "Airport"]
    ]

getStations :: [String] -> [Station] -> [Station]
getStations names stations =
    mapMaybe (\x -> find ((== x) . name) stations) names

shortestRoute :: String -> String -> [Station] -> [Station]
shortestRoute start end stations =
    case (find ((== start) . name) stations, find ((== end) . name) stations) of
        (Just s, Just e) -> shortestRoute' s e stations
        (Nothing, Just _) ->
            fail $ "Station " ++ start ++ " could not be found"
        (Just _, Nothing) -> fail $ "Station " ++ end ++ " could not be found"
        _                 -> fail "Start and end stations could not be found"
  where
    shortestRoute' :: Station -> Station -> [Station] -> [Station]
    shortestRoute' start end stations =
        minimumBy (\a b -> (length a) `compare` (length b))
            $ catMaybes
            $ possibleRoutes (getStations (routes start) stations) end [start] []
      where
        possibleRoutes :: [Station] -> Station -> [Station] -> [Maybe [Station]] ->[Maybe [Station]]
        possibleRoutes []       _   _   routes    = routes
        possibleRoutes (x : xs) end visited routes = if x `elem` visited
            then possibleRoutes xs end visited routes
            else if x == end
                then possibleRoutes xs end (visited ++ [x]) (routes ++ [Just (visited ++ [x])])
                else possibleRoutes xs end (visited ++ [x]) routes


main :: IO ()
main = do
    putStrLn "Enter Train Lines (separated with space), Start and Endpoint:"
    putStr "Line 1: "
    line1 <- getLine
    putStr "Line 2:"
    line2 <- getLine
    putStr "Start: "
    start <- getLine
    putStr "End: "
    end <- getLine
    print $ parseStations [words line1, words line2]
