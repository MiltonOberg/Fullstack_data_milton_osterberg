CREATE TABLE IF NOT EXISTS marts.views_per_country AS
 SELECT geografi, SUM("visningar") 
 AS "Visningar"
 FROM geografi.diagramdata
 GROUP BY geografi
 ORDER BY "Visningar"
 DESC;
  
 
 CREATE TABLE IF NOT EXISTS marts.top5_watched_videos AS
 SELECT videotitel, SUM("visningar")
 AS "Visningar"
 FROM innehall.tabelldata
 GROUP BY videotitel
 ORDER BY "Visningar"
 DESC LIMIT 6
 OFFSET 1;
 
CREATE TABLE IF NOT EXISTS marts.top5_click_exposure AS
 SELECT videotitel, "Klickfrekvens för exponeringar (%)"
 AS "click%"
 FROM innehall.tabelldata
 ORDER BY "click%"
 DESC LIMIT 5;