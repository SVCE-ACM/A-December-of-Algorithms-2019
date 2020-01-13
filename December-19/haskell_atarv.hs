{- December 19 - Periphery of a lake -}

import           Data.List

type Point = (Double, Double)

-- ccw > 0: points make up counter-clockwise turn
-- ccw = 0: points are collinear
-- ccw < 0: points make up clockwise turn
ccw :: Point -> Point -> Point -> Double
ccw (x1, y1) (x2, y2) (x3, y3) = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

-- find the point that forms a line with point 'a' such that there are no points
-- left of line formed by the point and point 'a'
findHullPoint :: Point -> Point -> [Point] -> Point
findHullPoint _ b [] = b
findHullPoint a b (x : xs) =
    if ccw a b x > 0 then findHullPoint a x xs else findHullPoint a b xs

convexHull :: [Point] -> [Point]
convexHull points =
    let startPoint = minimum points in giftWrap points startPoint [startPoint]
  where
    giftWrap :: [Point] -> Point -> [Point] -> [Point]
    giftWrap (x : xs) pointOnHull hull =
        let endpoint = findHullPoint pointOnHull x xs
        in  if endpoint == head hull
                then hull
                else giftWrap (delete endpoint (x : xs))
                            endpoint
                            (hull ++ [endpoint])

examplePoints :: [Point]
examplePoints =
    [(0, 3), (2, 2), (1, 1), (2, 1), (1, 2), (3, 0), (0, 0), (3, 3)]

main = do
    putStrLn "Enter coordinates (x,y) separated with space:"
    coords <- getLine >>= return . map (read) . words :: IO [Point]
    putStr "The outline is: "
    print $ convexHull coords
