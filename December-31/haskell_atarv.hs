{- December 31 - Build a city -}

import qualified Data.Text                     as T
import           Data.List
import           Data.Ord

type Point = (Double, Double)

distance :: Point -> Point -> Double
distance (x1, y1) (x2, y2) = sqrt $ (x1 - x2) ^ 2 + (y1 - y2) ^ 2

(.+.) :: Point -> Point -> Point
(.+.) (x1, y1) (x2, y2) = (x1 + x2, y1 + y2)

-- Index of minimum element
minIndex :: (Ord a, Num b, Enum b) => [a] -> b
minIndex xs = snd $ minimumBy (comparing fst) (zip xs [0 ..])

pointAvg :: [Point] -> Point
pointAvg (x : xs) =
    let (count, (xSum, ySum)) =
                foldl' (\(i, a) b -> (i + 1, a .+. b)) (1, x) xs
    in  (xSum / count, ySum / count)

kMeans :: [Point] -> [Point] -> [Point]
kMeans dataset centroids =
    let
        initClusters = zip [0 ..] $ replicate (length centroids) []
        clusters     = foldl
            (\clusts p ->
                insertTo clusts ((minIndex . map (distance p)) centroids) p
            )
            initClusters
            dataset
        newCentroids = map (pointAvg . snd) clusters
    in
        if centroids == newCentroids
            then centroids
            else kMeans dataset newCentroids

-- Insert `a` to nth cluster
insertTo :: Eq a1 => [(a1, [a2])] -> a1 -> a2 -> [(a1, [a2])]
insertTo indexedClusters nth a = map
    (\(i, set) -> if i == nth then (i, a : set) else (i, set))
    indexedClusters

-- Parse points from CSV-file
parseCsv :: (Read a, Read b) => String -> [(a, b)]
parseCsv =
    map (\[x, y] -> ((read . T.unpack) x, (read . T.unpack) y))
        . map (T.split (== ','))
        . T.lines
        . T.pack

main = do
    csvContents <- readFile "../src/res/build_city_csv.csv"
    let houses = parseCsv csvContents
    let stores = kMeans houses [(0, 0), (4, 4), (-4, -4)]
    mapM_ (\(i, s) -> putStrLn $ "Store " ++ show i ++ ": " ++ show s)
        $ zip [1 ..] stores
