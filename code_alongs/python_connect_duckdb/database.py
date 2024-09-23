import duckdb



class Database:
    def __init__(self, db_path) -> None:
        self.db_path = db_path
        self.connection = None
        
    def __enter__(self):
        # Starts connection
        self.connection = duckdb.connect(self.db_path)
        return self
    # Every thing that can happen inbetween
    def query(self, query):
        return self.connection.execute(query).fetchall()
    
    def __exit__(self, exc_type, exc_value, traceback):
        # Exits connection
        if self.connection:
            self.connection.close()
            
            
class DatabaseDataframe(Database):
    def query(self, query):
        return self.connection.execute(query).df()