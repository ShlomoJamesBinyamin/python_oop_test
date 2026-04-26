from iquerry import IQuerry
from logger import log
import sqlite3

class InsertQuery(IQuerry):
    def __init__(self, db_name):
        super().__init__(db_name)

    def create_connection(self):
        self.conn = sqlite3.connect(self.db_name)
        print("connection established")

    def connect(self):
        self.cursor = self.conn.cursor()
        print("cursor established")

    def commit(self, query):
        self.rows= self.cursor.execute(query)
        self.conn.commit()
        print(f"query {query} executed.")

    def fetch_results(self):
        pass

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
        print("connection closed")