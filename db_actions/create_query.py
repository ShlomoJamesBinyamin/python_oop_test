from iquerry import IQuerry
import sqlite3


class CreateQuery(IQuerry):

    def create_connection(self):
        self.conn = sqlite3.connect(self.db_name)
        print("connection established")

    def connect(self):
        self.cursor = self.conn.cursor()
        print("cursor established")

    def commit(self, query):
        self.cursor.execute(query)
        self.conn.commit()
        print(f"Query {query} executed successfully")

    def fetch_results(self):
        pass

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
        print("connection closed")