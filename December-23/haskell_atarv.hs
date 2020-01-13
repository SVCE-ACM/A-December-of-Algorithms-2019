{- December 23 - Finding the centroid of a polygon -}

type Point = (Double, Double)

-- Vertices must be in order of occurence on polygons perimeter!
-- Polygon must also be non-self-intersecting.
polygonArea :: [Point] -> Double
polygonArea vertices = 0.5 * shoelace (vertices ++ (take 1 vertices)) 0
  where
    shoelace [_] total = total
    shoelace ((x1, y1) : (x2, y2) : xs) total =
        shoelace ((x2, y2) : xs) (total + (x1 * y2 - x2 * y1))

centroid :: [Point] -> Point
centroid vertices =
    let area         = polygonArea vertices
        loopedAround = vertices ++ take 1 vertices
        cx           = (1 / (6 * area)) * xCoord loopedAround 0
        cy           = (1 / (6 * area)) * yCoord loopedAround 0
    in  (cx, cy)
  where
    xCoord [_] total = total
    xCoord ((x1, y1) : (x2, y2) : xs) total =
        xCoord ((x2, y2) : xs) (total + ((x1 + x2) * (x1 * y2 - x2 * y1)))
    yCoord [_] total = total
    yCoord ((x1, y1) : (x2, y2) : xs) total =
        yCoord ((x2, y2) : xs) (total + ((y1 + y2) * (x1 * y2 - x2 * y1)))

ex1 :: [Point]
ex1 = [(3, 4), (5, 2), (6, 7)]

ex2 :: [Point]
ex2 = [(0, 4), (0, 0), (4, 0), (4, 4)]

main = do
    putStr "Vertices: "
    print ex1
    putStr "Centroid: "
    print $ centroid ex1
    putStr "\nVertices: "
    print ex2
    putStr "Centroid: "
    print $ centroid ex2
