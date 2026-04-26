import sqlite3
from iquerry import IQuerry

class SelectQuery(IQuerry):

    def create_connection(self):
        self.conn = sqlite3.connect(self.db_name)
        print(f"connection specified.")

    def connect(self):
        self.cursor = self.conn.cursor()
        print(f"connection cursor applied.")

    def commit(self, query):
        print(f"running query...")
        self.rows= self.cursor.execute(query)

    def fetch_results(self):
        print("\nresults:")
        self.results = []
        for row in self.rows:
            self.results.append(row)
            print(row)

    def close_connection(self):
        self.cursor.close()
        self.conn.close()