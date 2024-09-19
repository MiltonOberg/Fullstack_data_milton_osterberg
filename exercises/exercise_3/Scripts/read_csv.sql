CREATE TABLE games AS (
SELECT
	*
FROM
	read_csv_auto('data/games.csv'));