import sqlite3
from db_actions.iquery import IQuery
from log_files.logger import log

class SelectQuery(IQuery):

    def create_connection(self):
        self.conn = sqlite3.connect(self.db_name)
        log.info(f"CONNECTION ESTABLISHED")

    def connect(self):
        self.cursor = self.conn.cursor()
        log.info(f"APPLIED CURSOR")

    def commit(self, query, params=None):
        self.rows= self.cursor.execute(query, params or ())
        log.info(f"RAN QUERY")

    def fetch_results(self):
        self.result = []
        for row in self.rows:
            self.result.append(row)
        log.info("QUERY FETCHED RESULTS") if self.result else log.info("NO FETCHED RESULTS")
        return self.result if self.result else None

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
        log.info("\nCONNECTION CLOSED")