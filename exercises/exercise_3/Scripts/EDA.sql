SELECT * FROM games;


SELECT
	DISTINCT winner
FROM
	games;


SELECT
	DISTINCT victory_status
FROM
	games;


SELECT
	COUNT(id)
FROM
	games;


SELECT
	COUNT(winner)
FROM
	games
GROUP BY
	winner;


SELECT
	opening_name,
	COUNT(*) AS count
FROM
	games
GROUP BY
	opening_name
ORDER BY
	count DESC
LIMIT 10;


SELECT
	GREATEST(white_rating,
	black_rating) AS highest_rating
FROM
	games
ORDER BY
	highest_rating DESC
LIMIT 1;


