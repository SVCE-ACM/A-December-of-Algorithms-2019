{- December 12 - Show JaSON the way -}
{-# LANGUAGE DeriveGeneric  #-}
{-# LANGUAGE DeriveAnyClass #-}
{-# LANGUAGE OverloadedStrings #-}

import           Data.Aeson -- stack install aeson
import           Data.Aeson.Types
import           GHC.Generics
import           Data.List                      ( find )
import           Data.Maybe                     ( isJust )
import           Data.Fixed                     ( mod' )
import qualified Data.ByteString.Lazy          as LB

type LatLon = (Double, Double) -- Coordinate
data Marker = Marker { name :: String, location :: LatLon }
    deriving (Show, Generic, ToJSON, FromJSON)

data Markers = Markers { markers :: [Marker] }
    deriving (Show, Generic, ToJSON, FromJSON)

data Direction = Direction { message :: String, distance :: Double, direction :: String}
    deriving (Show, Generic, ToJSON, FromJSON)

data Directions = Directions { directions :: [Direction] }
    deriving (Show, Generic, ToJSON, FromJSON)

-- Degrees to radians
degToRad :: Floating a => a -> a
degToRad = (*) (pi / 180.0)

-- Distance between two GPS points in kilometers
distanceKm :: LatLon -> LatLon -> Double
distanceKm (lat1, lon1) (lat2, lon2) =
    let
        earthRadius = 6371.0
        phi1        = degToRad lat1
        phi2        = degToRad lat2
        deltaPhi    = degToRad (lat2 - lat1)
        deltaLambda = degToRad (lon2 - lon1)
        a =
            (sin $ deltaPhi / 2) ^ 2
                + (cos phi1)
                * (cos phi2)
                * (sin $ deltaLambda / 2) ^ 2
        c = 2 * atan2 (sqrt a) (sqrt (1 - a))
    in
        earthRadius * c

-- Tells the direction of latter point in radians
bearing :: LatLon -> LatLon -> Double
bearing (lat1, lon1) (lat2, lon2) =
    let phi1        = degToRad lat1
        phi2        = degToRad lat2
        deltaLambda = degToRad (lon2 - lon1)
        theta       = atan2
            ((sin deltaLambda) * (cos phi2))
            ( (cos phi1) * (sin phi2) - (sin phi1) * (cos phi2) * (cos deltaLambda))
    in  (theta + 360.0) `mod'` 360.0

-- Cardinal direction from radians
cardinalDirection :: Double -> String
cardinalDirection p 
    | p > pi / 4 && p <= 3 * pi / 4     = "N"
    | p > 3 * pi / 4 && p <= 5 * pi / 4 = "W"
    | p > 5 * pi / 4 && p <= 7 * pi / 4 = "S"
    | otherwise = "E"

main = do
    content <- LB.readFile "../src/res/JaSON.json"
    case decode content :: Maybe Markers of
        Nothing        -> fail "Failed to parse location markers"
        Just locations -> do
            let start = find ((=="start") . name) (markers locations)
            let dest = find ((=="destination") . name) (markers locations)
            case (start, dest) of
                (Nothing   , Nothing  ) -> fail "no start nor destination"
                (Nothing   , _        ) -> fail "no start"
                (_         , Nothing  ) -> fail "no destination"
                (Just start, Just dest) -> do
                    let distanceBetween = distanceKm (location start) (location dest)
                    let dir = cardinalDirection $ bearing (location start) (location dest)
                    let direction = Direction { message   = "Da wae"
                                              , distance  = distanceBetween
                                              , direction = dir
                                              }
                    LB.writeFile "Directions.json" (encode (Directions [direction]))
