{-- haskell notes

to install GHCup (main installer for Haskell)
    curl --proto '=https' --tlsv1.2 -sSf https://get-ghcup.haskell.org | sh
--}

import Data.List ( sort )

testLists :: ([Integer], [Integer])
testLists = (
        [3, 4, 2, 1, 3, 3],
        [4, 3, 5, 3, 9, 3]
    )

testFileContents :: String
testFileContents = "3 4\n 4 3\n 2 5\n 1 3\n 3 9\n 3 3\n"

parseRawFileString :: String -> ([Int], [Int])
parseRawFileString rawFileString = (evenIndexedLocationIntegers, oddIndexedLocationIntegers)
    where
        evenIndexedLocationIntegers = map snd $ filter (even . fst) indexedLocationIntegers
        oddIndexedLocationIntegers = map snd $ filter (odd . fst) indexedLocationIntegers
        indexedLocationIntegers = zip [0..] $ map (read :: String -> Int) $ words rawFileString

sumOfAbsolutePairwiseDifferences :: ([Int], [Int]) -> Int
sumOfAbsolutePairwiseDifferences (xs, ys) = sum $ zipWith (curry (abs . uncurry (-))) (sort xs) (sort ys)

main :: IO()
main = do
    rawDataFileContents <- readFile "day_1_raw_data.csv"
    print $ sumOfAbsolutePairwiseDifferences $ parseRawFileString rawDataFileContents