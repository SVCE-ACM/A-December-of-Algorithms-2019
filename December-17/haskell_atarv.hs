{- December 17 - Subway Surfer -}

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
        (\a -> if name a == x
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
        minimumBy (\a b -> length a `compare` length b)
            $ catMaybes
            $ possibleRoutes (getStations (routes start) stations)
                             end
                             stations
                             [start]
                             []

possibleRoutes
    :: [Station]
    -> Station
    -> [Station]
    -> [Station]
    -> [Maybe [Station]]
    -> [Maybe [Station]]
possibleRoutes []       _   _        _       result = result
possibleRoutes (x : xs) end stations visited result = if x `elem` visited
    then possibleRoutes xs end stations visited result
    else if name x == name end
        then
            (result ++ [Just (visited ++ [x])])
                ++ possibleRoutes xs end stations visited result
        else
            possibleRoutes (getStations (routes x) stations)
                           end
                           stations
                           (visited ++ [x])
                           result
                ++ possibleRoutes xs end stations visited result

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
    let stations = parseStations [words line1, words line2]
    let route    = shortestRoute start end stations
    putStr "Fastest route: "
    putStrLn $ intercalate " -> " $ map name route
