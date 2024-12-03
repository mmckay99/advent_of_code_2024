-- haskell notes
-- to install GHCup (main installer for Haskell): curl --proto '=https' --tlsv1.2 -sSf https://get-ghcup.haskell.org | sh



main :: IO()
main = do
    rawDataFile <- readFile "day_1_raw_data.csv"
    print rawDataFile