desc;

SELECT
	*
FROM
	information_schema.schemata;

CREATE SCHEMA IF NOT EXISTS marts;

CREATE TABLE IF NOT EXISTS marts.content_view_time AS 
(
SELECT
	Videotitel,
	"Publiceringstid för video" AS Publiceringstid,
	Visningar,
	"Visningstid (timmar)" AS Visningstid_timmar,
	Exponeringar,
	Prenumeranter,
	"Klickfrekvens för exponeringar (%)" AS "Klickfrekvens_exponering_%"
FROM
	innehall.tabelldata
ORDER BY
	"Visningstid (timmar)" DESC OFFSET 1);

CREATE TABLE IF NOT EXISTS marts.views_per_date AS (
SELECT
	STRFTIME('%Y-%m-%d',
	Datum) AS Datum,
	Visningar
FROM
	innehall.totalt);


CREATE TABLE IF NOT EXISTS marts.top5_click_exposure AS
SELECT videotitel, "Klickfrekvens för exponeringar (%)"
AS "click%"
FROM innehall.tabelldata
ORDER BY "click%"
DESC LIMIT 5;

SELECT * FROM marts.top5_click_exposure


CREATE TABLE IF NOT EXISTS marts.views_per_country AS
SELECT geografi, SUM("visningar") 
AS "Visningar"
FROM geografi.diagramdata
GROUP BY geografi
ORDER BY "Visningar"
DESC;


SELECT * FROM marts.views_per_country


CREATE TABLE IF NOT EXISTS marts.top5_watched_videos AS
SELECT videotitel, SUM("visningar")
AS "Visningar"
FROM innehall.tabelldata
GROUP BY videotitel
ORDER BY "Visningar"
DESC LIMIT 6
OFFSET 1;


SELECT * FROM marts.top5_watched_videos

SELECT
	*
FROM
	information_schema.tables
WHERE
	table_schema = 'marts';

SELECT
	*
FROM
	marts.content_view_time;


SELECT
	*
FROM
	marts.views_per_date;
