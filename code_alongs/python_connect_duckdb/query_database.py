from database import Database_dataframe
from constants import DATABASE_PATH


class Query_database:
    def __init__(self, sql_query) -> None:
        with Database_dataframe(DATABASE_PATH) as db:
            self.df= db.query(sql_query)