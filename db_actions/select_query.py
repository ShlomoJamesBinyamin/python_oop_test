import sqlite3
from iquerry import IQuerry
from log_files.logger import log

class SelectQuery(IQuerry):

    def create_connection(self):
        self.conn = sqlite3.connect(self.db_name)
        log.info(f"connection specified.")

    def connect(self):
        self.cursor = self.conn.cursor()
        log.info(f"connection cursor applied.")

    def commit(self, query, params=None):
        log.info(f"running select query...")
        self.rows= self.cursor.execute(query, params)

    def fetch_results(self):
        log.info("\nresults:")
        self.results = []
        for row in self.rows:
            self.results.append(row)
            print(row)
        return self.results if self.results else None

    def close_connection(self):
        self.cursor.close()
        self.conn.close()