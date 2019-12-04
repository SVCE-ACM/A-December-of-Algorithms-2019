{- 
    December 5 - Convert CSV data to a HTML table 
    Command line arguments can be given in ghci with:
        :set args filename.csv
        main
-}
import           Prelude
import qualified Data.Text                     as T
import           Data.Maybe
import           System.Environment

-- Removes quotations from around text
removeQuotations :: T.Text -> T.Text
removeQuotations t =
    (fromMaybe t . T.stripSuffix quote)
        . (fromMaybe t . T.stripPrefix quote)
        $ t
    where quote = T.pack "\""

-- Create HTML-tags with given name, content inserted between tags
htmlTag :: String -> T.Text -> T.Text
htmlTag name content = T.concat
    [T.pack $ "<" ++ name ++ ">", content, T.pack $ "</" ++ name ++ ">"]

-- Concatenate cells to one table row
tableRow :: [T.Text] -> T.Text
tableRow cells = T.concat [T.pack "<tr>", T.concat cells, T.pack "</tr>"]

-- Transform from CSV to HTML table
csvToHtmlTable :: String -> T.Text
csvToHtmlTable csv =
    let rows         = lines csv
        cells        = map (T.splitOn (T.singleton ',') . T.pack) rows
        cleanedCells = map (map $ removeQuotations . T.strip) cells
        headerRow    = head cleanedCells
        tableRows    = drop 1 cleanedCells
        headersHtml  = T.concat $ map (htmlTag "th") headerRow
        rowsHtml     = map (tableRow . map (htmlTag "td")) tableRows
        table        = T.unlines (headersHtml : rowsHtml)
    in  htmlTag "html" $ htmlTag "body" $ htmlTag "table" table

main :: IO ()
main = do
    args <- getArgs
    let path = head args
    content <- readFile path
    writeFile "./output.html" $ (T.unpack . csvToHtmlTable) content
