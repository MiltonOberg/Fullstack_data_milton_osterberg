# Backend

### Change_name_data
Vi tittar ifall clean_data existerar. Om den gör det använder vi rmtree för att ta bort den ochh sedan skapa en ny cleaned_data där vi lägger in mapparna från raw_data med de uppdaterade namnen


### Constants
Path till databasen och till cleaned_data


### Database
I denna map har vi två klasser Database som hhanterar anslutningen med databasen ochh gör det möjligt att utföra queries inom with block.
Och den andra en underklass som gör det möjligt att ta ut data från basen till daraframes. Den används med query_database i utils


### Ingest_data_to_database
Här tar vi varje mapp och fil i cleaned_data, översätter/byter ut alla å, ä, ö. Efter det tar vi enskild fil och tar ut ett table name. Och med Databas klassen, tittar ifall schemat för denna data mapp finns sedan ifall tabellen i schemat finns, och annars skapar dessa två.


# Frontend

### Graph dict
Denna fil har jag förr att lätt kunna välja vilken diagram man vill titta på i dashboarden. Och denna är kopplad till graphs.


### Graphs
Här ligger de olika diagrammen för dashboarden.


### KPI
Denna fil är skapade metrics, kpier för dashboarden.

### Pages_dictionary
Här har jag ett dict för sido menyn i dashboarden med de olika sidovalen.

### Pages
Här är då layouten för de olika sidorna. Som då kallas beroende på vad för sida man väljer i denna meny.

### Style
Den css style med lite olika färger och storlekar på titlar och rubriker.


## Dashboard
Här har vi layouten för den faktiska dashboarden. Där resten av backend och frontend "används".




### Scripts
Dessa ligger i backend. Det finns en till Scripts mapp men den läggs till varje gång jag startar dbeaver.
