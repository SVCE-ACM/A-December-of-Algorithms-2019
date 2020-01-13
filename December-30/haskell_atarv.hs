{- December 30 - Minimize Pipe Cost -}

import           Data.List

type Cost = Int
data Edge a = Edge (a, a) Cost deriving (Show, Eq)

instance Ord a => Ord (Edge a) where
    (Edge _ costA) `compare` (Edge _ costB) = costA `compare` costB

uniqVertices :: (Eq a, Foldable t) => t (Edge a) -> [a]
uniqVertices edges = nub $ foldl (\v (Edge (a, b) _) -> v ++ [a, b]) [] edges

formsCycle :: (Eq a) => Edge a -> [Edge a] -> Bool
formsCycle (Edge (a, b) _) tree = null $ [a, b] \\ uniqVertices tree

minimizeCost :: (Show a, Ord a) => [Edge a] -> Cost
minimizeCost edges =
    let vertexCount         = (length . uniqVertices) edges
        -- Graph is a tree if |E| = |V - 1|
        minimumSpanningTree = kruskalMst (vertexCount - 1) (sort edges) []
    in  foldl (\total (Edge _ cost) -> total + cost) 0 minimumSpanningTree
  where
    kruskalMst _         []       mstSet = mstSet
    kruskalMst vrtxCount (e : es) mstSet = if length mstSet == vrtxCount
        then mstSet
        else if formsCycle e mstSet
            then kruskalMst vrtxCount es mstSet
            else kruskalMst vrtxCount es (e : mstSet)

exampleInput :: [Edge Char]
exampleInput =
    [ Edge ('S', 'A') 1
    , Edge ('S', 'B') 5
    , Edge ('S', 'C') 20
    , Edge ('A', 'C') 15
    , Edge ('B', 'C') 10
    ]

main = do
    sequence_
        $ [ putStrLn "["
          , sequence_ $ map (\x -> putStr ",     " >> print x) exampleInput
          , putStrLn "]"
          ]
    print $ minimizeCost exampleInput
